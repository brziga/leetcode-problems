# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        iterator = iter(letters)
        ans = 0
        for letter in iterator:
            min_i, max_i = None, None
            i = 0
            while i < len(s) and s[i] != letter: i += 1
            min_i = i
            i = len(s) - 1
            while i >= 0 and s[i] != letter: i -= 1
            max_i = i
            if min_i >= max_i: continue
            ans += len(set(s[min_i + 1 : max_i]))
        return ans