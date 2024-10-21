# https://leetcode.com/problems/find-closest-number-to-zero/description/

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        small = nums[0]
        for i in nums[1::]:
            if abs(i) < abs(small):
                small = i
            elif abs(i) == abs(small):
                if i > small:
                    small = i
        return small