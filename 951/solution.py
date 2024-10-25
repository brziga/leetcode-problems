# https://leetcode.com/problems/flip-equivalent-binary-trees/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2: return True # both null
        elif not root1 or not root2 or root1.val != root2.val: return False
        # dfs, no flips
        nfl = Solution.flipEquiv(self, root1.left, root2.left)
        nfr = Solution.flipEquiv(self, root1.right, root2.right)
        # flip and dfs
        yfl = Solution.flipEquiv(self, root1.right, root2.left)
        yfr = Solution.flipEquiv(self, root1.left, root2.right)
        
        return (nfl and nfr) or (yfl and yfr)