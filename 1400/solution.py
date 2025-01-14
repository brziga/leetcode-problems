# https://leetcode.com/problems/construct-k-palindrome-strings/

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False 
        chars = Counter(s)
        odds = 0
        for _, occ in chars.items():
            if occ % 2 == 1: odds += 1
            if odds > k: return False
        return True