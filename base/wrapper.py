# coding:utf-8

"""
闭包
    当某个函数被当成对象返回时，夹带了外部变量，就形成了一个闭包
装饰器
    应用:是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等...
    作用:为已经存在的对象添加额外的功能
"""


import time
from functools import wraps


def wrapper(fool):
    @wraps(fool)  # 避免被装饰函数自身的信息丢失。不加:in_fun;添加:fool
    def in_fun(*args, **kwargs):
        start_time = time.time()  # 测试性能
        res = fool(*args, **kwargs)
        end_time = time.time()
        print("run time", (end_time - start_time))
        return res
    return in_fun


@wrapper
def fool(a, b):  # 修饰带参数的函数
    time.sleep(2)
    result = a * b
    print("result", result)


@wrapper
def fool1():
    time.sleep(4)
    print("from fool")


def wrapper_1(fool2):
    return lambda: "<p>"+fool2()+"</p>"


def wrapper_2(fool2):
    return lambda: "<br>"+fool2()+"</br>"


def wrapper_3(fool2):
    return lambda: "<i>"+fool2()+"</i>"


# 事务处理:多个装饰器
@wrapper_1
@wrapper_2
@wrapper_3
def fool2():
    return ("i love lin")


# 类装饰器
class Decorator(object):
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("520")  # 打印日志
        self.f()
        print("love lin")


@Decorator
def fool3():
    print("1314")


fool(3, 4)
print(fool.__name__)
fool1()
print(fool2())
fool3()
