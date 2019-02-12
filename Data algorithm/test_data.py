def chang_str(string):
    string1 = "i love lin"
    print(string1)
    return


str = "lin love me"
# chang_str(str)
# print(str)


def quick_list(list1):
    if len(list1) < 1:
        return list1

    less = []
    base = list1.pop()
    max = []

    for i in list1:
        if i < base:
            less.append(i)
        else:
            max.append(i)

    return quick_list(less) + [base] + quick_list(max)


if __name__ == '__main__':
    lis = [1, 2, 6, 3, 4, 5, 9, 6]
    a = quick_list(lis)
    print(a)
