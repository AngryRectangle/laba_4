def merge(array, start, end):
    l = end - start
    result = list(array)
    h = l // 2
    i = 0
    j = 0
    k = 0
    while i + j < l:
        if j == l - h or array[i + start] < array[j + start + h] and i < h:
            result[k + start] = array[i + start]
            i += 1
        else:
            result[k + start] = array[j + start + h]
            j += 1
        k += 1

    for i in range(start, end):
        array[i] = result[i]


def mergeSort(array, start, end):
    l = end - start
    if l == 1:
        return

    mergeSort(array, start, start + l // 2)
    mergeSort(array, start + l // 2, end)
    merge(array, start, end)