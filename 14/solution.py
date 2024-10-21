# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        longestString = 200
        for strn in strs:
            longestString = len(strn) if len(strn) < longestString else longestString
        pref = ""
        for i in range(0, longestString):
            checking = strs[0][0:i+1]
            for strn in strs:
                if checking != strn[0:i+1]:
                    return pref
            pref = checking
        return pref