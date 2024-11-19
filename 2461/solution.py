# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        i = 0
        occs = {key: 0 for key in nums} # occurrences
        for n in nums[0:k]:
            occs[n] += 1
        subsum = sum(nums[0:k])
        uniques = len(set(nums[0:k]))
        res = subsum if uniques == k else res
        while i + k < len(nums):
            subsum += nums[i+k] - nums[i]
            occs[nums[i]] -= 1
            if occs[nums[i]] == 0:
                uniques -= 1
            if occs[nums[i+k]] == 0:
                uniques += 1
            occs[nums[i+k]] += 1
            if uniques == k:
                res = subsum if subsum > res else res
            i += 1
        return res