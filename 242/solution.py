# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = dict(Counter(list(s)))
        tSet = dict(Counter(list(t)))
        return sSet == tSet