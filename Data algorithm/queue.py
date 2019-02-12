# coding:utf-8
"""队列:先入先出"""


class Que(object):
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加新的元素到队列"""
        self.__list.append(item)  # O(n)
        # self.__list.insert(0, item)  # O(1)

    def pop(self):
        """弹出队列元素"""
        return self.__list.pop(0)  # O(1)
        # return self.__list.pop()  # O(n)

    def peek(self):
        """返回队列元素"""
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
        """返回队列的大小"""
        return len(self.__list)


class Dqueue(object):
    """双端队列"""
    def __init__(self):
        self.__list = []
        
    def add_front(self, item):
        self.__list.insert(0, item)
    
    def add_rear(self, item):
        self.__list.append(item)
        
    def del_front(self):
        return self.__list.pop(0)
        
    def del_rear(self):
        return self.__list.pop()
        
    def is_empty(self):
        if self.__list:
            return False
        else:
            return True

    def size(self):
        return len(self.__list)
        

if __name__ == "__main__":
    s = Que()
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

    m = Dqueue()
    print(" ")
    print(m.is_empty())
    m.add_front(1)
    m.add_front(3)
    m.add_front(5)
    m.add_rear(2)
    m.add_rear(4)
    m.add_rear(7)
    m.add_rear(8)
    print(m.del_front())
    print(m.del_rear())
    print(m.is_empty())
    print(m.size())
