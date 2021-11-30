def maxDepth(arr):
    depth = [0] * len(arr)
    stack = list()
    stack.extend(range(0, len(arr)))
    while len(stack) > 0:
        current = stack[len(stack) - 1]
        if depth[current] > 0:
            stack.pop()
            continue

        next = arr[current]
        if next == -1:
            depth[current] = 1
            stack.pop()
            continue

        if depth[next] < 1:
            stack.append(next)
            continue

        depth[current] = depth[arr[current]] + 1
        stack.pop()
    return max(depth)


file = open("input.txt", "r")
file.readline()
values = list(int(number) for number in file.readline().split())
write = open("output.txt", "w")
write.write(str(maxDepth(values)))
file.close()
write.close()
