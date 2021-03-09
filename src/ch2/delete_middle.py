def delete_middle(node):
    while node:
        node.data = node.next.data
        node.next = node.next.next

        node = node.next
