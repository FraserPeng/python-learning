'''
用 asyncio 提供的 @asyncio.coroutine 可以把一个 generator 标记为
coroutine 类型，然后在 coroutine 内部用 yield from 调用另一个 coroutine
实现异步操作。

请注意， async 和 await 是针对 coroutine 的新语法，要使用新的语法，
只需要做两步简单的替换：
1. 把 @asyncio.coroutine 替换为 async ；
2. 把 yield from 替换为 await 。
'''

# 异步

import threading
import asyncio


async def hello(n):
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(n)
    print('Hello again! (%s)' % threading.currentThread())


# 获取 EventLoop:
loop = asyncio.get_event_loop()
tasks = [hello(1), hello(2)]
# 执行 coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
