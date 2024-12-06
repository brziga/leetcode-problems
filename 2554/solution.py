# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        allowed = set(range(1, n + 1)) - set(banned)
        iterable = sorted(list(allowed))
        s = 0
        i = 0
        while i < len(iterable) and s <= maxSum:
            s += iterable[i]
            i += 1
        return i if s <= maxSum else i - 1