# https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateLevels(self, root, lvl, lvlSums=[]):
        if root is None: return
        if len(lvlSums) <= lvl:
            lvlSums.append(0)
        lvlSums[lvl] += root.val
        Solution.calculateLevels(self, root.left, lvl+1, lvlSums)
        Solution.calculateLevels(self, root.right, lvl+1, lvlSums)

    def updateTree(self, root, father, lvl, lvlSums, newrt):
        if root is None: return
        # print(root)
        # print(lvl, lvlSums[lvl])
        # print(father.left, father.right)
        if father.left:
            # print("left:", father.left.val, end=" | ",)
            a = father.left.val
        else:
            a = 0
        if father.right:
            # print("right:", father.right.val)
            b = father.right.val
        else:
            b = 0
        newrt.val = lvlSums[lvl] - a - b
        # print(newrt)
        newrt.left = copy.copy(root.left)
        newrt.right = copy.copy(root.right)
        # print("newroot", newrt)
        # print("root", root, "\n")
        Solution.updateTree(self, root.left, root, lvl+1, lvlSums, newrt.left)
        Solution.updateTree(self, root.right, root, lvl+1, lvlSums, newrt.right)

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelSums = []
        Solution.calculateLevels(self, root, 0, levelSums)
        # print(levelSums)
        newroot = TreeNode(0, copy.copy(root.left), copy.copy(root.right))
        Solution.updateTree(self, root.left, root, 1, levelSums, newroot.left)
        Solution.updateTree(self, root.right, root, 1, levelSums, newroot.right)
        return newroot