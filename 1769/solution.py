# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        pre_moves = [0] * n
        pre_balls = [int(x) for x in boxes]
        for i in range(1, n):
            pre_balls[i] += pre_balls[i - 1]
            pre_moves[i] = pre_balls[i - 1] + pre_moves[i - 1]
        
        post_moves = [0] * n
        post_balls = [int(x) for x in boxes[::-1]]
        for i in range(1, n):
            post_balls[i] += post_balls[i - 1]
            post_moves[i] = post_balls[i - 1] + post_moves[i - 1]
        post_moves = post_moves[::-1]

        ans = [pre_moves[i] + post_moves[i] for i in range(n)]
        return ans