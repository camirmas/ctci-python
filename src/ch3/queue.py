class Queue:

    def __init__(self):
        self.first = None
        self.last = None


    def add(self, data):
        node = QueueNode(data)
        if not self.first:
            self.first = node
            self.last = node
        else:
            self.last.next = node


    def remove(self):
        if self.first:
            data = self.first.data
            self.first = self.first.next
            if not self.first:
                self.last = None

            return data

        return self.first


    def peek(self):
        if self.first:
            return self.first.data
        return self.first


    def is_empty(self):
        return not self.first and not self.last


class QueueNode:

    def __init__(self, data):
        self.data = data
        self.next = None
