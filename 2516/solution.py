# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        occs = Counter(s)
        if k == 0: return 0
        elif not ('a' in occs.keys() and 'b' in occs.keys() and 'c' in occs.keys()) or not (occs['a'] >= k and occs['b'] >= k and occs['c'] >= k) : return -1

        n = len(s)
        res = n + 1
        left = 0
        for right in range(n):
            occs[s[right]] -= 1
            while min(occs.values()) < k:
                occs[s[left]] += 1
                left += 1
            res = min(res, n - (right - left + 1))
        return res