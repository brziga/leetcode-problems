# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

class Solution:
    def shortestPath(self, edges, n):
        queue = [(0, 0)]
        shortest = n - 1
        visited = set()
        while queue:
            q = queue.pop(0)
            if q[0] == n - 1:
                shortest = q[1] if q[1] < shortest else shortest
            elif q[0] not in visited:
                visited.add(q[0])
                for i in edges[q[0]]:
                    if i not in visited: queue.append((i, q[1] + 1))
        return shortest

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        edges = {i: [i+1] for i in range(n-1)}
        ans = []
        for q in queries:
            edges[q[0]].append(q[1])
            ans.append(self.shortestPath(edges, n))
        return ans