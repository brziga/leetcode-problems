# https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for e in arr:
            if e*2 in s or e/2 in s: return True
            s.add(e)
        return False