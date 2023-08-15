def copyRandomList(head):
    # two pass and hashmap
    oldToCopy = {None: None}
    cur = head

    while cur:
        copy = Node(cur.val)
        oldToCopy[cur] = copy
        cur = cur.next

    cur = head
    while cur:
        copy = oldToCopy[cur]
        copy.next = oldToCopy[cur.next]
        copy.random = oldToCopy[cur.random]
        cur = cur.next

    return oldToCopy[head]