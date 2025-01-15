# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        m = 0
        count = collections.Counter(s)
        zeros, ones = 0, count["1"]
        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros += 1
            else:
                ones -= 1
            m = zeros + ones if zeros + ones > m else m
        return m