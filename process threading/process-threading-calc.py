from threading import Thread
from multiprocessing import Pool
from time import *


def get_value():
    result = 0
    start_time = time()
    for i in range(100000):
        result += (1+2**i+i*33)

    stop_time = time()
    sum_time = stop_time - start_time
    print("result:%s and time:%s" % (result, sum_time*3))
    print("length of result:", len(str(result)))


def get_value_by_thread(name):
    result = 0

    for i in range(100000):
        result += (1+2**i+i*33)

    print("the Name:%s result:%s" % (name, result))


def get_value_by_process(name):
    result = 0

    for i in range(100000):
        result += (1 + 2 ** i + i * 33)

    print("the Name:%s result:%s" % (name, result))


if __name__ == '__main__':
    get_value()
    pool = Pool(3)
    start_time = time()
    for i in range(3):
        pool.apply_async(get_value_by_process(), args=("p1",))

    print("等待所有子进程完成...")
    pool.close()
    pool.join()
    stop_time = time()
    sum_time = stop_time - start_time

    print("进程总共耗时:%s" % sum_time)

    start_time1 = time()
    thread_list = []
    for i in range(3):
        t = Thread(target=get_value_by_thread(), args=("t"+str(i),))
        thread_list.append(t)

    for j in thread_list:
        j.start()

    for j in thread_list:
        j.join()

    stop_time1 = time()
    sum_time1 = stop_time1 - start_time1

    print("线程总共耗时:%s" % sum_time1)
