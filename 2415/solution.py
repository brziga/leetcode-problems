# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderTraversal(self, root) -> List:
        queue = [root]
        result = []
        while queue:
            curr = queue.pop(0)
            result.append(curr.val)
            if curr.left and curr.right:
                queue.append(curr.left)
                queue.append(curr.right)
        return result

    def treeFromList(self, lst) -> TreeNode:
        root = TreeNode(lst[0])
        index = 1
        queue = [root]

        while queue and index < len(lst):
            curr = queue.pop(0)

            curr.left = TreeNode(lst[index])
            queue.append(curr.left)
            index += 1

            curr.right = TreeNode(lst[index])
            queue.append(curr.right)
            index += 1
        
        return root

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        array = self.levelOrderTraversal(root)
        i, j, n = 0, 0, len(array)
        while 2 ** i < n:
            if i % 2 == 1:
                array[j:j+2**i] = array[j:j+2**i][::-1]
            j += 2 ** i
            i += 1
        return self.treeFromList(array)