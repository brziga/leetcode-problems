# https://leetcode.com/problems/string-compression-iii/

class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        prev = word[0]
        count = 1
        for c in word[1:]:
            if c == prev:
                if count < 9:
                    count += 1
                else:
                    comp += str(count) + prev
                    count = 1
            else:
                comp += str(count) + prev
                prev = c
                count = 1
        comp += str(count) + prev
        return comp