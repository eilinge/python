from multiprocessing import Pipe, Pool
import time


def send_pip1(pipe):
    while True:
        for i in range(10):
            print("pip1 will send:%d" % i)
            pipe.send(i)
            time.sleep(1)


def send_pip2(pipe):
    while True:
        for j in range(20, 40, 2):
            print("pip2 will send:%d" % j)
            pipe.send(j)
            time.sleep(1)


def recv_pip1(pipe):
    while True:
        print("pip1 will recv the :%s" % (pipe.recv()))
        time.sleep(1)


def recv_pip2(pipe):
    while True:
        print("pip2 will recv the :%s" % pipe.recv())
        time.sleep(1)


if __name__ == '__main__':
    pipes = Pipe()  # 全双工

    my_pool = Pool(4)

    my_pool.apply_async(send_pip1, args=(pipes[0],))  # connect1 发包
    my_pool.apply_async(recv_pip2, args=(pipes[1],))  # connect2 收包

    my_pool.apply_async(send_pip2, args=(pipes[1],))  # connect2 发包
    my_pool.apply_async(recv_pip1, args=(pipes[0],))  # connect1 收包

    my_pool.close()

    my_pool.join()
