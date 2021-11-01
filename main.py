import task_1
import helper
import merge
import sys

sys.setrecursionlimit(3000)
sizes = [10 ** 3, 10 ** 4, 10 ** 5]
for size in sizes:
    arr = helper.rand_array(size, 0, 2)
    copy = list(arr)
    mergeTime = helper.execution_time(lambda: merge.mergeSort(copy, 0, size - 1))
    copy = list(arr)
    quickSortOldTime = helper.execution_time(lambda: task_1.rand_quick_sort_old(copy, 0, size - 1))
    copy = list(arr)
    quickSortTime = helper.execution_time(lambda: task_1.rand_quick_sort(copy, 0, size - 1))
    print(
        f'Sorting times for n = {size}: merge - {mergeTime} quick sort 2 - {quickSortOldTime} quick sort 3 - {quickSortTime}')
