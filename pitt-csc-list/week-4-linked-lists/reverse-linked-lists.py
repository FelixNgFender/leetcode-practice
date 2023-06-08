# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    ptr = head
    prevPtr = None
    while ptr is not None:
        temp = ptr.next
        ptr.next = prevPtr
        prevPtr = ptr
        ptr = temp
    return prevPtr

