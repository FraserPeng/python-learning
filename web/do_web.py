from aiohttp import web
import asyncio
import logging
import json
logging.basicConfig(level=logging.INFO)

routes = web.RouteTableDef()


async def logger_factory(app, handler):
    async def logger(request):
        logging.info('Request: %s %s %s' %
                     (request.method, request.path, request))
        # await asyncio.sleep(0.3)
        return (await handler(request))
    return logger

# 响应处理
# 总结下来一个请求在服务端收到后的方法调用顺序是:
#     	logger_factory->response_factory->RequestHandler().__call__->get或post->handler
# 那么结果处理的情况就是:
#     	由handler构造出要返回的具体对象
#		然后在这个返回的对象上加上'__method__'和'__route__'属性，以标识别这个对象并使接下来的程序容易处理
#		RequestHandler目的就是从URL函数中分析其需要接收的参数，从request中获取必要的参数，调用URL函数,然后把结果返回给response_factory
#		response_factory在拿到经过处理后的对象，经过一系列对象类型和格式的判断，构造出正确web.Response对象，以正确的方式返回给客户端
# 在这个过程中，我们只用关心我们的handler的处理就好了，其他的都走统一的通道，如果需要差异化处理，就在通道中选择适合的地方添加处理代码


async def response_factory(app, handler):
    async def response(request):
        logging.info('Response handler...')
        r = await handler(request)
        logging.info('r = %s' % r)
        # 如果响应结果为web.StreamResponse类，则直接把它作为响应返回
        if isinstance(r, web.StreamResponse):
            logging.info(1)
            return r
        # 如果响应结果为字节流，则把字节流塞到response的body里，设置响应类型为流类型，返回
        if isinstance(r, bytes):
            logging.info(2)
            resp = web.Response(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        # 如果响应结果为字符串
        if isinstance(r, str):
            logging.info(3)
            # 先判断是不是需要重定向，是的话直接用重定向的地址重定向
            if r.startswith('redirect:'):
                return web.HTTPFound(r[9:])
            # 不是重定向的话，把字符串当做是html代码来处理
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        # 如果响应结果为字典
        if isinstance(r, dict):
            logging.info(4)
            # 先查看一下有没有'__template__'为key的值
            template = r.get('__template__')
            # 如果没有，说明要返回json字符串，则把字典转换为json返回，对应的response类型设为json类型
            if template is None:
                resp = web.Response(body=json.dumps(
                    r, ensure_ascii=False, default=lambda o: o.__dict__)
                    .encode('utf-8'))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
            else:
                # 如果有'__template__'为key的值，则说明要套用jinja2的模板，'__template__'Key对应的为模板网页所在位置
                resp = web.Response(body=app['__templating__'].get_template(
                    template).render(**r).encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                # 以html的形式返回
                return resp
        # 如果响应结果为int
        if isinstance(r, int) and r >= 100 and r < 600:
            return web.Response(r)
        # 如果响应结果为tuple且数量为2
        if isinstance(r, tuple) and len(r) == 2:
            t, m = r
            # 如果tuple的第一个元素是int类型且在100到600之间，这里应该是认定为t为http状态码，m为错误描述
            # 或者是服务端自己定义的错误码+描述
            if isinstance(t, int) and t >= 100 and t < 600:
                return web.Response(t, str(m))
        # default: 默认直接以字符串输出
        resp = web.Response(body=str(r).encode('utf-8'))
        resp.content_type = 'text/plain;charset=utf-8'
        return resp
    return response


@routes.get('/')
@routes.get('/{name}')
async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = {"Hello,": name}
    return web.json_response(text)


async def init(loop):
    app = web.Application(loop=loop, middlewares=[
        logger_factory, response_factory
    ])
    app.add_routes(routes)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1',
                                   8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
