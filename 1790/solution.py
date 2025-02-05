# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = 0
        dmap1 = set()
        dmap2 = set()
        for i in range(len(s1)):
            if s1[i] != s2[i]: 
                diffs += 1
                dmap1.add(s1[i])
                dmap2.add(s2[i])
            if diffs > 2: return False
        return (diffs == 0 or diffs == 2) and dmap1 == dmap2