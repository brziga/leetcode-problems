# https://leetcode.com/problems/ransom-note/description/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterMap = {}
        for letter in magazine:
            if letter in letterMap:
                letterMap[letter] += 1
            else:
                letterMap[letter] = 1
        for letter in ransomNote:
            if letter not in letterMap:
                return False
            else:
                letterMap[letter] -= 1
                if letterMap[letter] <= 0:
                    del letterMap[letter]
        return True