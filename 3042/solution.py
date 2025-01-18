# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            return str1 == str2[:len(str1)] and str1 == str2[-len(str1):]
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]): ans += 1
        return ans