def maxDepth(index, arr, depth):
    if depth[index] > 0:
        return

    depth[index] = True
    if arr[index] == -1:
        depth[index] = 1
        return

    maxDepth(arr[index], arr, depth)
    depth[index] = depth[arr[index]] + 1


file = open("input.txt", "r")
file.readline()
values = list(int(number) for number in file.readline().split())
depth = [0] * len(values)

write = open("output.txt", "w")
for i in range(0, len(values)): maxDepth(i, values, depth)
write.write(str(max(depth)))
file.close()
write.close()
