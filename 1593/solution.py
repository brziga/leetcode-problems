# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/

class Solution:
    def split(self, s: str, hm: set) -> int:
        if not s:
            return len(hm)
        
        max_splits = 0
        for i in range(1, len(s) + 1):
            ss = s[:i]
            if ss not in hm:
                hm.add(ss)
                max_splits = max(max_splits, self.split(s[i:], hm))
                hm.remove(ss)
                
        return max_splits

    def maxUniqueSplit(self, s: str) -> int:
        return self.split(s, set())
