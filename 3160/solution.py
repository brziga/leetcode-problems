# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {} #{i: 0 for i in range(limit + 1)}
        colors = {}
        ans = []
        for (x, y) in queries:
            if x in balls:
                colors[balls[x]] -= 1
                if colors[balls[x]] == 0: del colors[balls[x]]
            else:
                balls[x] = y
            colors[y] = colors.get(y, 0) + 1
            balls[x] = y
            ans.append(len(colors))
        return ans