class Node:
    next = None
    value = None


class LinkedQueue:
    start = None
    last = None

    count = 0
    middle = None

    def enqueue(self, value):
        self.count += 1
        elem = Node()
        elem.value = value
        if self.start is None:
            self.start = elem
            self.middle = elem
        else:
            self.last.next = elem
        self.last = elem

        if self.count % 2 != 0 and self.count > 1:
            self.middle = self.middle.next

    def dequeue(self):
        self.count -= 1
        if self.start is None:
            raise Exception("Queue is empty")
        value = self.start.value
        self.start = self.start.next
        if self.count % 2 != 0 and self.count > 1:
            self.middle = self.middle.next
        return value

    def middleQueue(self, value):
        self.count += 1
        elem = Node()
        elem.value = value
        next = self.middle.next
        self.middle.next = elem
        elem.next = next
        if self.count % 2 != 0 and self.count > 1:
            self.middle = self.middle.next

s = LinkedQueue()
file = open("input.txt", "r")
result = []
data = file.readline()
for line in file.readlines():
    data = line.split()
    if data[0][0] == "+":
        s.enqueue(int(data[1]))
    elif data[0][0] == "-":
        result.append(str(s.dequeue()))
    else: s.middleQueue(int(data[1]))

write = open("output.txt", "w")
write.write("\n".join(result))