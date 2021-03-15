class Stack:

    def __init__(self):
        self.top = None


    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node


    def pop(self):
        data = self.top.data
        self.top = self.top.next

        return data

    
    def peek(self):
        if self.top:
            return self.top.data
        return self.top

    
    def is_empty(self):
        return not self.top


class StackNode:

    def __init__(self, data):
        self.data = data
        self.next = None
