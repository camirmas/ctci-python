class Stack:

    def __init__(self):
        self.top = None


    def push(self, data):
        if not self.top:
            self.top = Node(data, data)
        else:
            new_top = Node(data, self.top.data)
            new_top.next = self.top
            self.top = new_top


    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            return data
        
        return self.top


    def peek(self):
        if self.top:
            return self.top.data

        return self.top

    
    def min(self):
        if self.top:
            return self.top.min
        
        return self.top

    
    def is_empty(self):
        return not self.top


class Node:

    def __init__(self, data, prev_min):
        self.data = data
        self.next = None

        if data < prev_min:
            self.min = data
        else:
            self.min = prev_min
