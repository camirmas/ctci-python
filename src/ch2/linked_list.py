class LinkedList:

    def __init__(self):
        self.head = None
    

    def add(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            node = self.head

            while node.next:
                node = node.next
            
            node.next = Node(data)


    def get(self, idx):
        counter = 0
        node = self.head

        while node:
            if counter == idx:
                return node

            node = node.next
            counter += 1
        
        return False

    
    def remove(self, idx):
        counter = 0

        node = self.head
        current = node

        if not self.head:
            return self.head

        if idx == 0:
            self.head = self.head.next
            return self.head

        while node.next:
            if counter+1 == idx:
                node.next = node.next.next
                return self.head
            
            node = node.next
            counter += 1

        return self.head




class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
