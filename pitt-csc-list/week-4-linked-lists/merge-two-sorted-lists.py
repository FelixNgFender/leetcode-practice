# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None or list2 is None:
            return list1 or list2
        ptr1 = list1
        ptr2 = list2
        sentry = ListNode()
        ptr = sentry
        while ptr1 and ptr2:
            ptr.next = ListNode(min(ptr1.val, ptr2.val))
            ptr = ptr.next
            if ptr1.val < ptr2.val:
                ptr1 = ptr1.next
            else:
                ptr2 = ptr2.next
        if ptr1:
            while ptr1:
                ptr.next = ListNode(ptr1.val)
                ptr = ptr.next
                ptr1 = ptr1.next
        else:
            while ptr2:
                ptr.next = ListNode(ptr2.val)
                ptr = ptr.next
                ptr2 = ptr2.next
        return sentry.next