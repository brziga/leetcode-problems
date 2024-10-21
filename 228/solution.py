# https://leetcode.com/problems/summary-ranges/description/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        currentStart = nums[0]
        currentEnd = nums[0]
        ranges = []
        for n in nums[1::]:
            if n == currentEnd+1:
                currentEnd = n
            else:
                ranges.append(f"{currentStart}" if currentStart == currentEnd else f"{currentStart}->{currentEnd}")
                currentStart = n
                currentEnd = n
        ranges.append(f"{currentStart}" if currentStart == currentEnd else f"{currentStart}->{currentEnd}")
        return ranges