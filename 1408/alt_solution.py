# https://leetcode.com/problems/string-matching-in-an-array/

# alternative solution with the (attempted) use of the KMP algorithm
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def computeLPS(pattern):
            m = len(pattern)
            LPS = [0] * m
            length = 0
             
            i = 1
            while i < m:
                if pattern[i] == pattern[length]:
                    length += 1
                    LPS[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = LPS[length - 1]
                    else:
                        LPS[i] = 0
                        i += 1
            
            return LPS
        
        def KMPSearch(text, pattern, LPS = None):
            n, m = len(text), len(pattern)
            if not LPS:
                LPS = computeLPS(pattern)
            i, j = 0, 0

            while i < n:
                if text[i] == pattern[j]:
                    i += 1
                    j += 1
                
                if j == m:
                    # match
                    return True
                    # if we wanted all the matches, we would instead append the index to a results list 
                    # and continue matching, but here we are only interested if there exists a match
                
                elif i < n and text[i] != pattern[j]:
                    if j != 0:
                        j = LPS[j - 1]
                    else:
                        i += 1
            
            return False
        
        ans = set()
        for word in words:
            LPS = computeLPS(word)
            for sword in words:
                if sword == word: continue
                elif KMPSearch(sword, word, LPS):
                    ans.add(word)
                    break
        return list(ans)