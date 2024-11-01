# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        sa = list(s) # string to array
        c = 1 # counter
        prev = None # previous
        result = ""
        for i in range(len(sa)):
            if sa[i] == prev:
                c += 1
            else:
                prev = sa[i]
                c = 1
            if c < 3:
                result += sa[i]
        
        return result