class Node:
    next = None
    value = None


class LinkedStack:
    current = None

    def isEmpty(self):
        return self.current is None

    def push(self, value):
        elem = Node()
        elem.value = value
        elem.next = self.current
        self.current = elem

    def pop(self):
        temp = self.current
        self.current = self.current.next
        return temp.value

    def last(self):
        return self.current.value

    def __str__(self):
        res = []
        temp = self.current
        while temp is not None:
            res.append(str(temp.value))
            temp = temp.next

        result = ""
        for i in range(len(res) - 1, 0, -1):
            result += res[i] + " "

        if len(res) > 0:
            result += res[0]
        return result


class LinkedQueue:
    start = None
    last = None

    def enqueue(self, value):
        elem = Node()
        elem.value = value
        if self.start is None:
            self.start = elem
        else:
            self.last.next = elem
        self.last = elem

    def dequeue(self):
        if self.start is None:
            raise Exception("Queue is empty")
        value = self.start.value
        self.start = self.start.next
