# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lr = [1] * len(nums)
        rl = [1] * len(nums)
        for i in range(1, len(nums)):
            lr[i] = lr[i-1] * nums[i-1]
            rl[-i-1] = rl[-i-1+1] * nums[-i-1+1]
        # print(lr, rl)
        prods = [0] * len(nums)
        for i in range(0, len(nums)):
            prods[i] = lr[i] * rl[i]
        return prods