def reorderList(head):
    # Reverse latter half and start stitching
    def reverse(head):
        left, right = None, head
        while right:
            temp = right.next
            right.next = left
            left = right
            right = temp
        return left

    if not head or not head.next:
        return

    # pseudo tortoise and hare
    slow = fast = head
    prevSlow = None
    while fast and fast.next:
        fast = fast.next.next
        prevSlow = slow
        slow = slow.next
    # slow now points at mid point
    prevSlow.next = reverse(slow)

    start, end = head, prevSlow.next
    # stitching
    while start != prevSlow:
        temp1, temp2 = start.next, end.next
        start.next = end
        end.next = temp1
        start, end = temp1, temp2
    start.next = end
    return
