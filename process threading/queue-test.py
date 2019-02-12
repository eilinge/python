# 使用进程池实现数据共享
from multiprocessing import Pool, Manager
import os
import time


def write_f1(q):
    print("当前子进程{}".format(os.getpid()))
    for i in ["A", "B", "C"]:
        print('writeFs1 Put %s to queue' % i)
        q.put(i)
        time.sleep(1)


def write_f2(q):
    print("当前子进程{}".format(os.getpid()))
    for i in ["E", "F", "G"]:
        print('writeFs2 Put %s to queue' % i)
        q.put(i)
        time.sleep(1)


def read_fs(q):
    print("当前子进程{}".format(os.getpid()))
    while not q.empty():
        value = q.get()
        print("readFs get value:%s from queue " % value)
        time.sleep(1)


if __name__ == '__main__':
    print("当前父进程{}".format(os.getpid()))
    q = Manager().Queue() # Manger().Queue()  消息队列可用于进程池

    my_pool = Pool(3)
    my_pool.apply_async(write_f1,args=(q,))
    my_pool.apply_async(write_f2, args=(q,))
    my_pool.apply_async(read_fs, args=(q,))

    my_pool.close()
    my_pool.join()
