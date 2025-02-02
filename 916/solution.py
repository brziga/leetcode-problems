# https://leetcode.com/problems/word-subsets/

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        letters_b = {}
        for b in words2:
            l_b = Counter(b)
            for letter, occ in l_b.items():
                if letter not in letters_b:
                    letters_b[letter] = occ
                else:
                    letters_b[letter] = occ if occ > letters_b[letter] else letters_b[letter]

        ans = []
        for a in words1:
            if letters_b.keys() <= set(a):
                letters_a = Counter(a)
                is_subset = True
                for letter, occ in letters_b.items():
                    if occ > letters_a[letter]:
                        is_subset = False
                        break
                if is_subset: ans.append(a)
        return ans