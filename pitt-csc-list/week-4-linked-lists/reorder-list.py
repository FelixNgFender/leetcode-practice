# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        def reverse(head):
            if head is None or head.next is None:
                return head
            curr, prev = head, None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        if head is None or head.next is None:
            return head
        fast, slow, prevSlow = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            prevSlow = slow
            slow = slow.next
        prevSlow.next = reverse(slow)

        start, end = head, prevSlow.next
        while start != prevSlow:
            temp1 = start.next
            start.next = end
            temp2 = end.next
            end.next = temp1
            start = temp1
            end = temp2
        start.next = end
        return head
