# https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(("a", "e", "i", "o", "u"))
        n = len(words)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i + 1] += 1

        ans = [0] * len(queries)
        for i in range(len(queries)):
            l, r = queries[i]
            ans[i] = prefix[r + 1] - prefix[l]
        return ans
