# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900,
        }
        sub_pairs = "IV", "IX", "XL", "XC", "CD", "CM"
        if len(s) == 1: return conversion[s]
        res = 0
        i = 0
        while i < len(s):
            if i == len(s)-1: 
                res += conversion[s[i]]
                break
            if s[i:i+2] in sub_pairs:
                res += conversion[s[i:i+2]]
                i += 2
            else:
                res += conversion[s[i]]
                i += 1
        return res