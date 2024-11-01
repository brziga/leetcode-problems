# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.hmap = {}
        self.sizes = {}
        self.val2id = {}
        self.id2val = {}

    def dfs(self, root, h):
        if not root: return 0
        self.val2id[root.val] = len(self.hmap)
        self.id2val[len(self.hmap)] = root.val
        self.hmap[root.val] = h
        leftside = self.dfs(root.left, h + 1)
        rightside = self.dfs(root.right, h + 1)
        self.sizes[root.val] = 1 + leftside + rightside
        return 1 + leftside + rightside

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.dfs(root, 0)
        # print(self.hmap)
        # print(self.sizes)
        # print(self.val2id)

        n = len(self.hmap)
        left, right = [0] * n, [0] * n
        for i in range(n):
            left[i] = self.hmap[self.id2val[i]]
            if i > 0:
                left[i] = max(left[i-1], left[i])
        
        for i in range(n-1, -1, -1):
            right[i] = self.hmap[self.id2val[i]]
            if i < n - 1:
                right[i] = max(right[i], right[i + 1])


        answers = []
        for q in queries:
            size = self.sizes[q] - 1
            qid = self.val2id[q]
            # left = list(self.hmap.values())[:qid]
            # right = list(self.hmap.values())[qid+1+size:]
            # h = max(left + right)
            li, ri = qid, qid + size
            h = max(
                0,
                left[li - 1] if li > 0 else 0,
                right[ri + 1] if ri < n - 1 else 0
            )
            answers.append(h)
        return answers