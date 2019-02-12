# coding:utf-8


from time import ctime, sleep
import threading


class MyThread(threading.Thread):
    def __init__(self, func, args, name=' '):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        threadLock.acquire()
        self.func(*self.args)
        threadLock.release()


def super_player(file, stime):
    for i in range(2):
        print('Start Playing:%s %s' % (file, ctime()))
        test1(file)
        test2(file)
        sleep(stime)


def test1(a):
    s1 = a * a
    print('s1:%s %s' % (s1, ctime()))


def test2(a):
    s2 = a * a
    print('s2:%s %s' % (s2, ctime()))


threadLock = threading.RLock()
list = {2: 3, 5: 4}

threads = []
for (v, k) in list.items():
    t = MyThread(super_player, (v, k), super_player.__name__)
    threads.append(t)

if __name__ == '__main__':
    for i in range(len(list)):
        threads[i].start()
    for i in range(len(list)):
        threads[i].join()

    print('the end:%s' % ctime())
