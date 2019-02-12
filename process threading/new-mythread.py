import time
import threading


def lighter():  #
    t = 0
    while True:
        if t < 5:
            F1.clear()
            print("红灯亮")
        elif t >= 5 and t < 10:
            F1.set()
            print("绿灯亮")
        else:
            t = 0
            continue
        # print(t)
        t += 1
        time.sleep(1)


def car(*args):
    F1.clear()  # 最开始要清除标志位
    while True:
        if F1.is_set():  # 判断是否设置了标志位
            print("宝马走")
            time.sleep(1)

        else:
            print("等待")
            F1.wait()  # 会不断查找标志是否存在。如果没有标志位，就一直卡在这里，不会执行下面的
            print("准备")


F1 = threading.Event()  # 设置一个Event实例

L = threading.Thread(target=lighter, )

C = threading.Thread(target=car, args=("宝马",))

L.start()
C.start()
