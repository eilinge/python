# -*- coding:utf-8 -*-
'''
#产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：
#“子程序就是协程的一种特例。”
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) #一旦生产了东西，通过c.send(n)切换到consumer执行
        print('[PRODUCER] Consumer return: %s' % r)
    c.close() #通过c.close()关闭consumer，整个过程结束。

c = consumer()
produce(c)
'''
# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，
# 然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。


# 用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，
# 然后在coroutine内部用yield from调用另一个coroutine实现异步操作。

'''
import asyncio

@asyncio.coroutine  #coroutine协同程序
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(2)
    print("Hello again!")

async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")
# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()

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
'''

import asyncio
# @asyncio.coroutine yield from == async await 异步I/O


async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
