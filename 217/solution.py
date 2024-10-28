# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = set()
        result = False
        for n in nums:
            if n in hmap: return True
            else: hmap.add(n)
        return result