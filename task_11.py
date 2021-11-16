class Node:
    next = None
    value = -1


file = open("input.txt", "r")
result = []
data = file.readline().split()
lasted = int(data[1])
queue = list(map(lambda x: int(x), file.readline().split()))
current = Node()
current.value = queue[0]
last = current
file.close()
for i in range(1, len(queue)):
    n = Node()
    n.value = queue[i]
    last.next = n
    last = n

while lasted > 0:
    if current is None:
        break

    lasted -= 1
    current.value -= 1
    next = current.next
    if current.value > 0:
        last.next = current
        current.next = None
        last = current
    elif current.next is None:
        break

    if next is not None:
        current = next

sum = 0
temp = current
while temp is not None and temp.value > 0:
    sum += 1
    temp = temp.next

write = open("output.txt", "w")
write.write(str(sum) + "\n")
if sum == 0:
    write.write("-1")
else:
    temp = current
    while temp is not None:
        result.append(str(temp.value))
        temp = temp.next
    write.write(" ".join(result))
