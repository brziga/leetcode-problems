# https://leetcode.com/problems/number-of-ways-to-split-array/

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        
        post = [0] * (n + 1)
        for i in range(n, 0, -1):
            post[i - 1] = post[i] + nums[i - 1]

        splits = 0
        for i in range(n - 1):
            if pre[i + 1] >= post[i + 1]: splits += 1
        return splits