file = open("input.txt", "r")
file.readline()
values = list(int(number) for number in file.readline().split())
isHeap = True
l = len(values)
for i in range(1, l // 2 + 1):
    if values[i-1] <= values[i * 2] and (2 * i + 1 >= l or values[i-1] <= values[i * 2 + 1]):
        continue

    isHeap = False
    break

write = open("output.txt", "w")
write.write("YES" if isHeap else "NO")
file.close()
write.close()
