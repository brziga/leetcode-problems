# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = [root]
        nextlevel = []
        current = queue
        ans = [[root.val]]
        currans = []
        while queue or nextlevel:
            c = queue.pop(0)
            if c.left: 
                nextlevel.append(c.left)
                currans.append(c.left.val)
            if c.right: 
                nextlevel.append(c.right)
                currans.append(c.right.val)
            if not queue:
                queue, nextlevel = nextlevel, queue
                if currans: ans.append(currans)
                currans = []         
        return ans