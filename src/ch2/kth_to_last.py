def kth_to_last(l, k):
    l_len = l.len()

    if k > l_len:
        return None

    count = 0
    node = l.head
    idx = l_len - k

    while node:
        if count == idx:
            return node
        
        node = node.next
        count += 1

    return None
