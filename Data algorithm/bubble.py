# -*- coding:utf-8 -*-
"""数据算法:1.排序方法;2.遍历次数"""


def bubble(list1):
    """冒泡排序:1.遍历列表中的每个元素,进行比较,将最大的元素放到最后;2.最后遍历的元素必定最小"""
    ll = len(list1)
    for _ in range(ll-1):  # 最后比较的元素必定最小
        for i in range(ll-1):  # 每次比较2个数
            if list1[i] > list1[i+1]:
                list1[i+1], list1[i] = list1[i], list1[i+1]

    return list1


def select_sort(list1):
    """选择排序:1.使用索引遍历列表中的每个元素,从开始比较位置与后面元素比较,将最小的元素放在开始比较位置;2.最后遍历的元素必定最大."""
    n = len(list1)
    for j in range(n-1):  # 最后比较的元素必定最大
        min_index = j
        for i in range(j+1, n):  # 从开始位置进行比较
            if list1[min_index] > list1[i]:
                list1[min_index], list1[i] = list1[i], list1[min_index]

    return list1


def insert_sort(list1):
    """插入排序:1.使用索引遍历列表中的每个元素,将后面元素与前一个元素比较,假使小于前一个元素,则往前逐一移动继续比较;
               2.假使前面元素已排好顺序,如果大于则直接退出(最优时间复杂度)"""
    n = len(list1)
    for j in range(1, n):
        i = j
        while i > 0:
            if list1[i] < list1[i-1]:
                list1[i], list1[i-1] = list1[i-1], list1[i]
                i -= 1  # 假使小于前一个元素,则往前逐一移动继续比较
            else:
                break  # (最优时间复杂度)假使前面元素已排好顺序,如果大于则直接退出

    return list1


def shell_sort(list1):
    """希尔排序(特殊的插入排序):1.引入步长,分组进行比较;2.步长为1->插入排序"""
    n = len(list1)
    group = n // 4

    while group > 0:
        for j in range(group, n):
            # j = group group+1 group+2 group+3 ... n-1
            # 4567 89
            # group1 =4 a[0] a[4] a[8]
            i = j
            while i > 0:
                if list1[i] < list1[i-group]:
                    list1[i], list1[i-group] = list1[i-group], list1[i]
                    i -= group
                else:
                    break  # 假使前面元素已排好顺序,如果大于则直接退出
        # 缩短步长
        group = group // 2

    return list1


def quick_sort(list1, first, last):
    """快速排序:1.选择一个基数,对原有列表进行排序分离;2.使用递归对已排好列表逐渐细分再排序"""
    if first >= last:
        return

    low = first
    high = last
    mid_value = list1[first]

    # 取出每次已排序列表的第一个元素,找到其相应位置
    while low < high:
        # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
        while low < high and list1[high] > mid_value:
            high -= 1

        # 如找到,则把第high个元素赋值给第个元素i,此时表中low,high个元素相等
        list1[low] = list1[high]

        # 同样的方式比较前半区
        while low < high and list1[low] <= mid_value:
            low += 1
        list1[high] = list1[low]

    # 做完第一轮比较之后,列表被分成了两个半区,并且low=high,需要将这个数设置回base
    list1[low] = mid_value

    # 对左边进行快排
    quick_sort(list1, first, low-1)
    # 对右边进行快排
    quick_sort(list1, low+1, last)

    return list1


def merge_sort(list1):
    """归并排序:1.将整体依次进行拆分,比较排序;2.将拆分排序之后的个体再合并成整体,再进行比较排序;3.采用递归"""
    n = len(list1)

    if n <= 1:
        return list1
    mid = n // 2

    left_list = merge_sort(list1[:mid])  # 先拆分成单个元素
    right_list = merge_sort(list1[mid:])  # 先拆分成单个元素

    print("left_list1", left_list)
    print("right_list1", right_list)

    """将已拆分成单个的元素,使用下标对列表进行比较,调整位置,合并再比较"""
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] > right_list[right_pointer]:
            result.append(right_list[right_pointer])
            right_pointer += 1
        else:
            result.append(left_list[left_pointer])
            left_pointer += 1

    """当下标结束,将剩下已排序的整体直接添加在后面"""
    result += left_list[left_pointer:]
    result += right_list[right_pointer:]
    print("result", result)
    return result


if __name__ == "__main__":
    l1 = [24, 12, 33, 1, 55, 122, 13, 66, 7, 44, 1]

    """
    使用内建函数进行排序
    print(sorted(list_1))
    l1.reverse()
    print(l1)
    l1.sort(reverse=True)
    print(l1)
    """

    print(bubble(l1))
    print(select_sort(l1))
    print(shell_sort(l1))
    print(merge_sort(l1))
    print(quick_sort(l1, 0, len(l1)-1))
