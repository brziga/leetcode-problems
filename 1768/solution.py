# https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        result = []
        while 1:
            result.append(word1[i])
            result.append(word2[i])
            i += 1
            if i >= len(word1):
                result.append(word2[i::])
                break
            elif i >= len(word2):
                result.append(word1[i::])
                break
        return "".join(result)