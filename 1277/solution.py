class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 1:
                    dp[y][x] = 1 if (y==0 or x==0) else 1 + min(dp[y-1][x], dp[y][x-1], dp[y-1][x-1])

        return sum([sum(line) for line in dp])