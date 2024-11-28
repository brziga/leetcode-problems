# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = [] # priority queue (min heap)
        heapq.heappush(pq, (0, 0, 0)) # (cost = num of obst., ycoord, xcoord)
        visited = {(0, 0): 0} # visited nodes and the lowest cost to them

        while pq:
            ccost, cy, cx = heapq.heappop(pq) # pop smallest --> current
            if (cy, cx) == (m - 1, n - 1): continue
            moves = []
            if cy > 0: # move up
                moves.append((ccost + grid[cy - 1][cx], cy - 1, cx))
            if cy < m - 1: # move down
                moves.append((ccost + grid[cy + 1][cx], cy + 1, cx))
            if cx > 0: # move left
                moves.append((ccost + grid[cy][cx - 1], cy, cx - 1))
            if cx < n - 1: # move right
                moves.append((ccost + grid[cy][cx + 1], cy, cx + 1))
            for mv in moves:
                mcost, my, mx = mv
                if (my, mx) not in visited or visited[(my, mx)] > mcost:
                    # if not yet visited or previously visited with higher cost
                    heapq.heappush(pq, mv)
                    visited[(my, mx)] = mcost
        
        return visited[(m - 1, n - 1)]