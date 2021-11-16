# Meaningless code....
stack = []
current = 0
capacity = 0


def add(elem):
    global current
    global capacity
    if current == capacity:
        ensureCapacity(max(1, capacity * 2))
    stack[current] = elem
    current += 1


def pop():
    global current
    val = stack[current - 1]
    current -= 1
    return val


def ensureCapacity(count):
    global capacity
    stack.append([] * (count - capacity))
    capacity = count


file = open("input.txt", "r")
result = []
count = int(file.readline())
for i in range(0, count):
    data = file.readline().split()
    if data[0] == "-":
        result.append(str(pop()))
    else:
        add(int(data[1]))

write = open("output.txt", "w")
write.write("\n".join(result))
file.close()
write.close()
