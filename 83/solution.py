# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = -101
        ptr = head
        prev = None
        while ptr:
            if ptr.val != seen:
                seen = ptr. val
                prev = ptr
            else:
                prev.next = ptr.next
            ptr = ptr.next
        return head