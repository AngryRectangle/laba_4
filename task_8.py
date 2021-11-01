import random


def swap(array, a, b, info):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp
    temp = info[a]
    info[a] = info[b]
    info[b] = temp


def partition_old(array, l, r, info):
    x = array[l]
    j = l
    for i in range(l + 1, r + 1):
        if array[i] <= x:
            j += 1
            swap(array, j, i, info)
    swap(array, l, j, info)
    return j


def rand_quick_sort_old(array, l, r, info):
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
            swap(array, l, k, info)
            m = partition_old(array, l, r, info)
            stack.append((l, m - 1))
            stack.append((m + 1, r))


file = open("input.txt")
raw = file.readline().split()
count = int(raw[1])

def point(line):
    data = line.split()
    return int(data[0]), int(data[1])


points = list(map(point, file.read().split('\n')))
file.close()
lengths = list(map(lambda x: x[0] * x[0] + x[1] * x[1], points))
infos = [0] * len(points)
for i in range(0, len(infos)):
    infos[i] = i
rand_quick_sort_old(lengths, 0, len(lengths) - 1, infos)
file = open("output.txt", "w")
str = ''
for i in range(0, count):
    print(f'{points[infos[i]]} sqr len {points[infos[i]][0] ** 2 + points[infos[i]][1] ** 2}')

file.write(','.join(map(lambda x: f'[{x[0]}, {x[1]}]', points[slice(0, count)])))


file.close()