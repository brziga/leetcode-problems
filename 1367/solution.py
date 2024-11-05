# https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def enqueue(self, root, queue):
        if not root: return
        queue.append(root)
        self.enqueue(root.left, queue)
        self.enqueue(root.right, queue)

    def check(self, root, head):
        if not head: return True
        if not root: return False
        result = root.val == head.val
        left = self.check(root.left, head.next)
        right = self.check(root.right, head.next)
        return result and (left or right)


    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        q = []
        self.enqueue(root, q)
        
        result = False
        for node in q:
            if not node: continue
            result = self.check(node, head)
            if result: return result
        return result