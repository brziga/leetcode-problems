# https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        p = len(pref)
        ans = 0
        for word in words:
            if word[:p] == pref: ans += 1
        return ans