# https://leetcode.com/problems/maximum-number-of-balloons/description/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {key: 0 for key in ('b', 'a', 'l', 'o', 'n')}
        for l in text:
            if l in letters:
                letters[l] += 1
        letters["l"] //= 2
        letters["o"] //= 2
        return sorted(letters.values())[0]