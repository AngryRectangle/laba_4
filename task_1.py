import random


def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


def partition_old(array, l, r):
    x = array[l]
    j = l
    for i in range(l + 1, r + 1):
        if array[i] <= x:
            j += 1
            swap(array, j, i)
    swap(array, l, j)
    return j


def rand_quick_sort_old(array, l, r):
    stack = list()
    stack.append((l, r))
    index = 0
    while index < len(stack):
        pair = stack[index]
        index += 1
        l = pair[0]
        r = pair[1]
        if l < r:
            k = random.randint(l, r)
            swap(array, l, k)
            m = partition_old(array, l, r)
            stack.append((l, m - 1))
            stack.append((m + 1, r))


def partition(array, l, r):
    x = array[l]
    j = l
    k = 1
    for i in range(l + 1, r + 1):
        if array[i] == x:
            j += 1
            swap(array, j, i)
            swap(array, l + k, j)
            k += 1
        elif array[i] < x:
            j += 1
            swap(array, j, i)

    for i in range(0, k):
        swap(array, l + i, j - i)
    return j - k + 1, j + 1


def rand_quick_sort(array, l, r):
    stack = list()
    stack.append((l, r))
    index = 0
    while index < len(stack):
        pair = stack[index]
        index += 1
        l = pair[0]
        r = pair[1]
        if l < r:
            k = random.randint(l, r)
            swap(array, l, k)
            s, e = partition(array, l, r)
            stack.append((l, s))
            stack.append((e, r))


arr = [0] * 100
for i in range(0, 100):
    arr[i] = random.randint(0, 1)

rand_quick_sort_old(arr, 0, len(arr) - 1)
for i in range(0, len(arr) - 1):
    if arr[i] > arr[i + 1]:
        print("error in sort")
        break
