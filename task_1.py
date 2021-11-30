file = open("input.txt", "r")
file.readline()
values = list(int(number) for number in file.readline().split())
isHeap = True
l = len(values)
for i in range(1, l):
    if values[(i - 1)//2] <= values[i]:
        continue

    isHeap = False
    break

write = open("output.txt", "w")
write.write("YES" if isHeap else "NO")
file.close()
write.close()
