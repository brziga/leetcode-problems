# https://leetcode.com/problems/count-number-of-bad-pairs/

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = {}
        good = 0

        for i in range(n := len(nums)):
            key = i - nums[i]
            good += count.get(key, 0)
            count[key] = count.get(key, 0) + 1
        
        return ((n * (n - 1)) // 2) - good