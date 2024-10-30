# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/description/

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        for col in range(n-2, -1, -1):
            for row in range(m):
                moves = ((row-1, col+1), (row, col+1), (row+1, col+1))
                for mv in moves:
                    if 0 <= mv[0] < m:
                        if grid[mv[0]][mv[1]] > grid[row][col]:
                            dp[row][col] = max(dp[row][col], 1 + dp[mv[0]][mv[1]])
        
        return max([r[0] for r in dp])