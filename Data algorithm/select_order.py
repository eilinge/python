def selection_sort(alist):
    n = len(alist)

    for i in range(n-1):
        limit_index = i
        if alist[limit_index] < alist[i]:
            alist[limit_index], alist[i] = alist[i], alist[limit_index]

        if alist[limit_index] < alist[i]:
            pass


alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]

selection_sort(alist)

print(alist)
