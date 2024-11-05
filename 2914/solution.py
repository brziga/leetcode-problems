# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

class Solution:
    def minChanges(self, s: str) -> int:
        ugly = 0
        for i in range(0, len(s), 2):
            if s[i:i+2] == "01" or s[i:i+2] == "10": ugly += 1
        return ugly