# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['U'] * n for _ in range(m)]
        for w in walls:
            r, c = w
            grid[r][c] = 'W'
        for g in guards:
            r, c = g
            grid[r][c] = 'G'

        for y in range(m):
            guarding = False
            for x in range(n):
                if grid[y][x] == 'W':
                    guarding = False
                    continue
                elif guarding:
                    grid[y][x] = 'g' if grid[y][x] != 'G' else 'G'
                elif grid[y][x] == 'G': 
                    guarding = True
            guarding = False
            for x in range(n - 1, -1, -1):
                if grid[y][x] == 'W':
                    guarding = False
                    continue
                elif guarding:
                    grid[y][x] = 'g' if grid[y][x] != 'G' else 'G'
                elif grid[y][x] == 'G': 
                    guarding = True

        for x in range(n):
            guarding = False
            for y in range(m):
                if grid[y][x] == 'W':
                    guarding = False
                    continue
                elif guarding:
                    grid[y][x] = 'g' if grid[y][x] != 'G' else 'G'
                elif grid[y][x] == 'G': 
                    guarding = True
            guarding = False
            for y in range(m - 1, -1, -1):
                if grid[y][x] == 'W':
                    guarding = False
                    continue
                elif guarding:
                    grid[y][x] = 'g' if grid[y][x] != 'G' else 'G'
                elif grid[y][x] == 'G': 
                    guarding = True

        return Counter([el for row in grid for el in row])['U']