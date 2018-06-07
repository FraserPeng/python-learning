# 异步

import threading
import asyncio


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


# 获取 EventLoop:
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 执行 coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
