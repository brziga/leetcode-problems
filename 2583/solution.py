# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

## doesn't run in this environment...

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    mp = {}
    def rec(self, root, lvl):
        if root is None: return
        if lvl not in self.mp.keys():
            self.mp[lvl] = root.val
        else:
            self.mp[lvl] += root.val
        Solution.rec(self, root.left, lvl+1)
        Solution.rec(self, root.right, lvl+1)

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        self.mp = {}
        Solution.rec(self, root, 0)
        print(self.mp)
        return sorted(self.mp.items(), key=lambda x: x[1], reverse=True)[k-1][1] if len(self.mp.keys()) >= k else -1