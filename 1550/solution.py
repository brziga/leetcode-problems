# https://leetcode.com/problems/three-consecutive-odds/description/

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c = 0
        for n in arr:
            if n % 2 == 1:
                c += 1
            else:
                c = 0
            if c >= 3: return True
        return False