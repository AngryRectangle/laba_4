class TrueStack:
    stack = []
    length = 0
    capacity = 0

    def add(self, elem):
        if self.length == self.capacity:
            self.ensureCapacity(max(1, self.capacity * 2))
        self.stack[self.length] = elem
        self.length += 1

    def pop(self):
        val = self.stack[self.length - 1]
        self.length -= 1
        return val

    def last(self):
        return self.stack[self.length - 1]

    def ensureCapacity(self, count):
        self.stack.extend([None] * (count - self.capacity))
        self.capacity = count

    def clear(self):
        self.length = 0