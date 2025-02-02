# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxes = None
    def dfs(self, root, depth = 0):
        if not root: return
        if depth not in self.maxes:
            self.maxes[depth] = root.val
        else:
            self.maxes[depth] = root.val if root.val > self.maxes[depth] else self.maxes[depth]
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.maxes = {}
        self.dfs(root, 0)
        return [pair[1] for pair in sorted(list(self.maxes.items()))]