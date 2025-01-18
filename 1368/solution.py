# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        adjacency = {}
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        for i in range(m):
            for j in range(n):
                adjacency[(i, j)] = []
                for d, (dx, dy) in enumerate(dirs):
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        weight = 0 if d == grid[i][j] - 1 else 1
                        adjacency[(i, j)].append((weight, (ni, nj)))

        heap = [(0, (0, 0))]
        min_cost = {(i, j): float("inf") for i in range(m) for j in range(n)} 
        min_cost[(0, 0)] = 0

        while heap:
            w, (cx, cy) = heapq.heappop(heap)
            if w > min_cost[(cx, cy)]:
                continue
            if cx == m - 1 and cy == n - 1:
                return w

            for nw, (nx, ny) in adjacency[(cx, cy)]:
                new_cost = w + nw
                if new_cost < min_cost[(nx, ny)]:
                    min_cost[(nx, ny)] = new_cost
                    heapq.heappush(heap, (new_cost, (nx, ny)))