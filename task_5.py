import task_1
import helper


def h_index(arr):
    task_1.rand_quick_sort(arr, 0, len(arr) - 1)
    m = 0
    for i in range(len(arr) - 1, 0, -1):
        m = max(m, min(len(arr) - i, arr[i]))
    return m


print(h_index(helper.rand_array(5000, 0, 1000)))
