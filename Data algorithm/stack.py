# coding:utf-8
"""栈:先入后出"""


class Stack(object):
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加新的元素到栈顶"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.is_empty() is not None:
            return self.__list[-1]
        else:
            return

    def is_empty(self):
        """判断是否为空"""
        if self.__list:
            return False
        else:
            return True

    def size(self):
        """返回栈的大小"""
        return len(self.__list)


if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(1)
    s.push(2)
    s.push(4)
    s.push(3)
    print(s.is_empty())
    print(s.size())
    print(s.peek())
    print(s.pop())
    print(s.peek())
