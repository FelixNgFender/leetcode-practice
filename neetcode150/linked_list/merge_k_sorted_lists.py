import heapq


def mergeKLists(lists):
    heap = []
    sentry = ListNode()
    ptr = sentry
    for i, list in enumerate(lists):
        if list:
            heapq.heappush(heap, (list.val, i))
    while heap:
        nx = (
            heapq.heappop(heap)
            if not lists[heap[0][1]].next
            else heapq.heapreplace(heap, (lists[heap[0][1]].next.val, heap[0][1]))
        )
        ptr.next = ListNode(nx[0])
        ptr = ptr.next
        lists[nx[1]] = lists[nx[1]].next
    return sentry.next


# Neetcode solution: merge pairs of linked lists
