# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            hm = {}
            for i in range(0, len(nums)):
                hm[nums[i]] = i
            for i in range(0, len(nums)):
                x = nums[i]
                y = target - x
                if y in hm.keys():
                    yi = hm[y]
                    if yi != i: return [i, yi]