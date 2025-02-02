# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: List[int]) -> bool:
        sections = [[nums[0]]]
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if len(sections) >= 2: return False
                sections[-1].append(nums[i - 1])
                sections.append([nums[i]])
        sections[-1].append(nums[-1])
        return len(sections) == 1 or sections[0][0] >= sections[1][1]