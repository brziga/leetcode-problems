# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], h = 1) -> int:
        if not root: return h - 1
        return max(
            self.maxDepth(root.left, h + 1),
            self.maxDepth(root.right, h + 1)
        )