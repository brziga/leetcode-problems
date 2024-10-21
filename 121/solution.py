# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    low = prices[0]
    mp = 0
    for i in range(1, len(prices)):
        e = prices[i]
        if e < low:
            low = e
        else:
            diff = e - low
            if diff > mp:
                mp = diff
    return mp