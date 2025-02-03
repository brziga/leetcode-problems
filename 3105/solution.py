# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest = 1
        curr_inc = 1
        curr_dec = 1
        for i in range(1, n := len(nums)):
            if nums[i] > nums[i - 1]:
                curr_inc += 1
                curr_dec = 1
                longest = curr_inc if curr_inc > longest else longest
            elif nums[i] < nums[i - 1]:
                curr_inc = 1
                curr_dec += 1
                longest = curr_dec if curr_dec > longest else longest
            else:
                curr_inc = 1
                curr_dec = 1
        return longest