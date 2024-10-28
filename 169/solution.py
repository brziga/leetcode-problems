# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occs = dict(Counter(nums))
        items = sorted(occs.items(), key = lambda x: x[1], reverse = True)
        return items[0][0]