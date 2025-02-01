# https://leetcode.com/problems/special-array-i/

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        parity = True
        for i in range(1, n:= len(nums)):
            if nums[i - 1] % 2 == nums[i] % 2:
                return False
        return parity