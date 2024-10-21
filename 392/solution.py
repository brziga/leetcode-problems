# https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i1, i2 = 0, 0
        while i1 < len(s) and i2 < len(t):
            if s[i1] == t[i2]:
                i1 += 1
                i2 += 1
            else:
                i2 += 1
        return i1 >= len(s)