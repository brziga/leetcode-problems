# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], res = None, carry = 0) -> Optional[ListNode]:
        if not res: res = []
        if not l1 and not l2:
            if carry > 0:
                res.append(carry)
            result = ListNode(res[0])
            itr = result
            for r in res[1:]:
                itr.next = ListNode(r)
                itr = itr.next
            return result
        elif not l1:
            a, b = 0, l2.val
            n1, n2 = l1, l2.next
        elif not l2:
            a, b = l1.val, 0
            n1, n2 = l1.next, l2
        else:
            a, b = l1.val, l2.val
            n1, n2 = l1.next, l2.next
        c = a + b + carry
        carry = c // 10
        c = c % 10
        res.append(c)
        return self.addTwoNumbers(n1, n2, res, carry)