swaps = []


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    swaps.append(str(a) + " " + str(b))


file = open("input.txt", "r")
file.readline()
values = list(int(number) for number in file.readline().split())
l = len(values)
stack = []
stack.extend(range(0, len(values) // 2))
while len(stack) > 0:
    i = stack.pop()
    childIndex = i * 2 + 1
    if childIndex >= l:
        continue

    minIndex = childIndex + 1 if childIndex + 1 < l and values[childIndex + 1] < values[childIndex] else childIndex
    if values[i] > values[minIndex]:
        swap(values, i, minIndex)
        stack.append(minIndex)


new_line = "\n"
write = open("output.txt", "w")
write.write(f"{len(swaps)} \n{new_line.join(swaps)}")
file.close()
write.close()

print(" ".join(str(value) for value in values))
