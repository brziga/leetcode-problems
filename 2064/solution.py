# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

class Solution:
    def canDistrib(self, n, quants, k):
        a = sum([math.ceil(q/k) for q in quants])
        if a <= n:
            return True
        return False
        
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)

        while l < r:
            mid = (l + r) // 2
            if self.canDistrib(n, quantities, mid):
                r = mid
            else:
                l = mid + 1
        return l