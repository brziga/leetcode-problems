# https://leetcode.com/problems/rotate-string/description/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        shifted = s
        for i in range(len(s)-1):
            if shifted == goal: return True
            shifted = shifted[1:] + shifted[0]
        return shifted == goal