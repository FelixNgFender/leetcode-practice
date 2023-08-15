def addTwoNumbers(l1, l2):
    ptr1, ptr2 = l1, l2
    sentry = ListNode()
    ptrRes = sentry
    carry = 0
    while ptr1 or ptr2:
        if not ptr1:
            result = ptr2.val + carry
        elif not ptr2:
            result = ptr1.val + carry
        else:
            result = ptr1.val + ptr2.val + carry
        if result >= 10:
            result = int(str(result)[-1])
            carry = 1
        else:
            carry = 0
        ptrRes.next = ListNode(result)
        ptrRes = ptrRes.next
        if not ptr1:
            ptr2 = ptr2.next
        elif not ptr2:
            ptr1 = ptr1.next
        else:
            ptr1, ptr2 = ptr1.next, ptr2.next
    if carry == 1:
        ptrRes.next = ListNode(carry)
    return sentry.next