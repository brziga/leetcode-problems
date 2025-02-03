# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1] + 1
        dp = [0] * n
        dayset = set(days)

        for i in range(1, n):
            if i in dayset:
                dpcost = dp[i - 1] + costs[0]
                dpcost = min(dpcost, dp[(i - 7) if i - 7 >= 0 else 0] + costs[1])
                dpcost = min(dpcost, dp[(i - 30) if i - 30 >= 0 else 0] + costs[2])
                dp[i] = dpcost
            else:
                dp[i] = dp[i - 1]
        
        return dp[-1]