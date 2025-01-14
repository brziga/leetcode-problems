# https://leetcode.com/problems/string-matching-in-an-array/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for word in words:
            for sword in words:
                if word != sword and word in sword: ans.add(word)
        return list(ans)