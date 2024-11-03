# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    out = None
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not self.out: self.out = []
        if not root: return self.out
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.out.append(root.val)
        return self.out