from threading import Thread
from queue import Queue
import threading
import time


def write_fs(q):
    print("当前子线程{}".format(threading.current_thread()))
    for i in ["A", "B", "C"]:
        print('Put %s to queue' % i)
        q.put(i)
        time.sleep(1)


def read_fs(q):
    print("当前子线程{}".format(threading.current_thread()))
    for _ in range(4):
        value = q.get()
        print("get value:%s from queue " % value)
        time.sleep(2)


if __name__ == '__main__':
    print("当前父线程{}".format(threading.current_thread()))

    q = Queue() # Queue() 只能用于父子线程
    p1 = Thread(target=write_fs, args=(q,))
    p2 = Thread(target=read_fs, args=(q,))
    p1.start()
    p1.join()

    p2.start()
    p2.join()
