import asyncio


async def tests():

    b = await a  # 异步执行操作
    print("c")

# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，
# 然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。

loop = asyncio.get_event_loop() #
tasks = [tests(), tests()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# @asyncio.coroutine yield from == async await 异步I/O
# yield from asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，
# 主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了

'''
import threading
import asyncio

#yield from asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，
#主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了
@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

Hello world! (<_MainThread(MainThread, started 11176)>)
Hello world! (<_MainThread(MainThread, started 11176)>)
Hello again! (<_MainThread(MainThread, started 11176)>)
Hello again! (<_MainThread(MainThread, started 11176)>)
'''