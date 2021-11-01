import math
import helper


def radix_sort(a, result, power, l, r, m_power):
    if power > m_power:
        return

    c = [0] * 10
    ten_powered = 10 ** power
    ten_less_powered = 10 ** (power - 1)
    for i in range(l, r):
        c[(a[i] % ten_powered) // ten_less_powered] += 1

    count = 0
    for j in range(0, 10):
        tmp = c[j]
        c[j] = count
        count += tmp

    for j in range(l, r):
        d = (a[j] % ten_powered) // ten_less_powered
        result[c[d] + l] = a[j]
        c[d] += 1

    for i in range(l, r):
        a[i] = result[i]

    last = 0
    radix_sort(a, result, power + 1, r, l, m_power)


def sort(a, b):
    res = [0] * len(a) * len(b)
    for i in range(0, len(res)):
        res[i] = a[i % len(a)] * b[i // len(a)]
    sum = 0
    n = [0] * len(res)
    max_power = math.ceil(math.log10(max(res)))
    radix_sort(res, n, 1, 0, len(n), max_power)
    for i in range(0, len(n), 10):
        sum += n[i]
    return sum


print(sort([7, 1, 4, 9], [2, 7, 8, 11]))
