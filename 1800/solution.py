# https://leetcode.com/problems/maximum-ascending-subarray-sum/

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s = nums[0]
        ms = nums[0]
        last = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > last:
                s += nums[i]
            else:
                ms = s if s > ms else ms
                s = nums[i]
            last = nums[i]
        ms = s if s > ms else ms
        return ms