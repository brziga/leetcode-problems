# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if len(nums) < 2: return len(nums)
        maxlen = 1
        i, s = 1, 0
        print(nums)
        while i < len(nums)-1:
            print(s, i, maxlen)
            if nums[i] != nums[i-1]+1:
                # not consecutive
                if len(nums[s:i]) > maxlen:
                    maxlen = len(nums[s:i])
                s = i
            i += 1
        print(s, i, maxlen)
        if nums[i] == nums[i-1]+1:
            if len(nums[s:i+1]) > maxlen:
                maxlen = len(nums[s:i+1])
        else:
            if len(nums[s:i]) > maxlen:
                maxlen = len(nums[s:i])
        return maxlen