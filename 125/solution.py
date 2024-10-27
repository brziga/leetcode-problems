# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = "" # converted string
        for c in s:
            if c.isalnum():
                cs += c.lower()
        return cs[:len(cs)//2] == cs[::-1][:len(cs)//2]