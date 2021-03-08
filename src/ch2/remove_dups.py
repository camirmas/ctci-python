from .linked_list import LinkedList


def remove_dups(l):
    nodes = []

    node = l.head

    while node and node.next:
        nodes.append(node.data)

        if node.next.data in nodes:
            node.next = node.next.next
            
        node = node.next

    return node
