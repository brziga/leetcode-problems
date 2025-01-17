# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # borrowed from 102
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
    
    def calcSwaps(self, unsorted):
        sortd = sorted(unsorted)
        n = len(unsorted)
        v2i = {sortd[i]: i for i in range(n)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or v2i[unsorted[i]] == i: continue

            cycle = 0
            x = i
            while not visited[x]:
                visited[x] = True
                x = v2i[unsorted[x]]
                cycle += 1
            
            if cycle > 1: swaps += cycle - 1
        
        return swaps

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        lot = self.levelOrder(root)
        swaps = 0
        for level in lot:
            swaps += self.calcSwaps(level)
        return swaps