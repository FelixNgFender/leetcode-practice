# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def reverseList(head):
    left, right = None, head
    while right:
        temp = right.next
        right.next = left
        left = right
        right = temp
    return left
