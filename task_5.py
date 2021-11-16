class TrueStack:
    stack = []
    length = 0
    capacity = 0

    def add(self, elem):
        if self.length == self.capacity:
            self.ensureCapacity(max(1, self.capacity * 2))
        prevMax = 0
        if self.length > 0:
            prevMax = max(self.stack[self.length - 1])
        self.stack[self.length] = (elem, prevMax)
        self.length += 1

    def pop(self):
        val = self.stack[self.length - 1]
        self.length -= 1
        return val[0]

    def last(self):
        return self.stack[self.length - 1]

    def ensureCapacity(self, count):
        self.stack.extend([None] * (count - self.capacity))
        self.capacity = count

    def maxFrom(self):
        return max(self.stack[self.length - 1])

    def clear(self):
        self.length = 0


tStack = TrueStack()
file = open("input.txt", "r")
result = []
count = int(file.readline())

for line in file.readlines():
    data = line.split()
    if data[0] == "push":
        tStack.add(int(data[1]))
    elif data[0] == "max":
        result.append(str(tStack.maxFrom()))
    elif data[0] == "pop":
        tStack.pop()

write = open("output.txt", "w")
write.write("\n".join(result))
file.close()
write.close()
