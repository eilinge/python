# coding:utf-8
"""二分法查找"""


def bubble(list1):
    ll = len(list1)

    for j in range(ll-1,0,-1):
        for i in range(j):
            if list1[i] > list1[i+1]:
                list1[i+1], list1[i] = list1[i], list1[i+1]

    return list1


def binary(a_list, item):
    """递归查找"""
    n = len(a_list)

    mid = n // 2
    if mid == 0:
        return False

    if item == a_list[mid]:
        return True
    elif item < a_list[mid]:
        return binary(a_list[:mid], item)
    else:
        return binary(a_list[mid+1:], item)


def binary_1(a_list, item):
    """非递归查找"""
    n = len(a_list)
    first = 0
    last = n-1
    while first <= last:
        mid = (first+last) // 2
        if item == a_list[mid]:
            return True
        elif item < a_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == "__main__":
    a_list = [12, 33, 1, 55, 122, 13, 66, 7, 44, 1]
    c1 = bubble(a_list)

    # print(binary(c1, 33))
    # print(binary(c1, 34))

    print(binary_1(c1, 33))
    print(binary_1(c1, 34))