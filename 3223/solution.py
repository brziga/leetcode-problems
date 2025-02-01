# https://leetcode.com/problems/minimum-length-of-string-after-operations/

class Solution:
    def minimumLength(self, s: str) -> int:
        hm = Counter(s)
        
        dels = 0
        for _, l in hm.items():
            if l >= 3:
                if l % 2 == 1:
                    dels += l - 1
                else:
                    dels += l - 2
        
        return len(s) - dels