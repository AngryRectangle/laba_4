import task_13

file = open("input.txt", "r")
buffer_size = int(file.readline().split()[0])


def toTuple(line):
    splitted = line.split()
    return int(splitted[0]), int(splitted[1])


values = list(toTuple(line) for line in file.readlines())
values.append((10**6 + 10**5 + 1, 0))
result = ["-1"] * len(values)
processorTime = 0
buffer = task_13.LinkedQueue()
i = 0
size = 0
for packet in values:
    startTime = packet[0]
    duration = packet[1]
    delta = startTime - processorTime
    while not buffer.isEmpty() and delta - buffer.first()[1] >= 0:
        current = buffer.dequeue()
        delta -= current[1]
        result[current[2]] = str(processorTime)
        processorTime += current[1]
        size -= 1

    if buffer.isEmpty():
        processorTime = startTime

    if size >= buffer_size:
        continue

    packet = packet[0], packet[1], i
    i += 1
    buffer.enqueue(packet)
    size += 1

result.pop()
write = open("output.txt", "w")
write.write("\n".join(result))
file.close()
write.close()
