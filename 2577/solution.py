# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = []
        heapq.heappush(pq, (0, 0, 0)) # (time, y, x)
        visited = set()
        if grid[0][1] > 1 and grid[1][0] > 1: return -1

        while pq:
            c, y, x = heapq.heappop(pq)
            if (y, x) == (m - 1, n - 1): return c
            moves = []
            if y > 0: # move up
                moves.append((c + 1, y - 1, x))
            if y < m - 1: # move down
                moves.append((c + 1, y + 1, x))
            if x > 0: # move left
                moves.append((c + 1, y, x - 1))
            if x < n - 1: # move right
                moves.append((c + 1, y, x + 1))
            for move in moves:
                mc, my, mx = move
                if (my, mx) in visited: continue
                if (diff := grid[my][mx] - c) > 0: # walrus ftw
                    mc = grid[my][mx] if diff % 2 == 1 else grid[my][mx] + 1
                heapq.heappush(pq, (mc, my, mx))
                visited.add((my, mx))
        return -1