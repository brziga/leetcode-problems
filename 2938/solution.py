# https://leetcode.com/problems/separate-black-and-white-balls/description/

class Solution:
    def minimumSteps(self, s: str) -> int:
        ic = 0 # intermediate count
        res = 0 # result
        for i in range(len(s)-1, -1, -1): # iterate backwards
            if s[i] == "0":
                ic += 1
            else:
                res += ic
        return res