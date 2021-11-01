### Task 1
Test results for recursion quick sort:
```
Sorting times for n = 1000: merge - 0.009999513626098633 quick sort 2 - 0.06802773475646973 quick sort 3 - 0.0019996166229248047
Sorting times for n = 10000: merge - 0.39402127265930176 quick sort 2 - #recursion_depth_error quick sort 3 - 0.01100015640258789
Sorting times for n = 100000: merge - 31.16899871826172 quick sort 2 - #recursion_depth_error quick sort 3 - 0.1149742603302002
```

Test results for iterative quick sort:
```
Sorting times for n = 1000: merge - 0.010998964309692383 quick sort 2 - 0.06500482559204102 quick sort 3 - 0.0010004043579101562
Sorting times for n = 10000: merge - 0.39600062370300293 quick sort 2 - 5.811608791351318 quick sort 3 - 0.01100015640258789
Sorting times for n = 100000: merge - 31.32999587059021 quick sort 2 - 525.6389484405518 quick sort 3 - 0.10199856758117676
```

### Task 5
Сложность алгоритма O(n^2) т.к такую сложность имеет quicksort в худшем случе, 
если использовать вместо него сортировку подсчётом, 
то можно достигнуть сложности O(n), но в этом нет смысла, т.к ограничений по времени нет.

Если бы массив был изначально отсортирован, то сложность составила бы O(n)

### Task 6
Использована radix sort со сложностью O(n)

### Task 7
Использовал radix sort для сортировки строк

### Task 8
Сортрую точки по расстоянию от центра через быструю сортировку и выбираю n ближайших