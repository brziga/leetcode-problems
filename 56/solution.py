# https://leetcode.com/problems/merge-intervals/description/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        result = []
        for intv in intervals[1::]:
            if intv[0] <= end:
                end = intv[1] if intv[1] > end else end
            else:
                result.append([start, end])
                start, end = intv
        result.append([start, end])
        return result