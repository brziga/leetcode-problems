# https://leetcode.com/problems/tuple-with-same-product/

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prods = {}
        for i in range(n := len(nums)):
            for j in range(i + 1, n):
                prods[nums[i] * nums[j]] = prods.get(nums[i] * nums[j], 0) + 1
        res = 0
        for _, occ in prods.items():
            if occ < 2: continue
            res += (
                ((occ * (occ - 1)) / 2)
                *
                8
            )
        return int(res)