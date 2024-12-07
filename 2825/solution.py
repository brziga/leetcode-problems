# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1): return False
        i, j = 0, 0
        n, m = len(str1), len(str2)
        while j < m:
            if i >= n: return False
            diff = ord(str2[j]) - ord(str1[i])
            diff = diff if diff != -25 else 1
            while not (0 <= diff <= 1):
                i += 1
                if i >= n: return False
                diff = ord(str2[j]) - ord(str1[i])
                diff = diff if diff != -25 else 1
            j += 1
            i += 1
        return True