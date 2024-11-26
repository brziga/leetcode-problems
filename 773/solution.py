# https://leetcode.com/problems/sliding-puzzle/

class Solution:
    def checkSolved(self, board):
        return (
            board[0][0] == 1 and
            board[0][1] == 2 and
            board[0][2] == 3 and
            board[1][0] == 4 and
            board[1][1] == 5 and
            board[1][2] == 0
        )

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        seen = set() # seen states
        queue = [(board, 0)]
        depth = 0 # ~ number of moves

        while queue:
            b, d = queue.pop(0)
            if self.checkSolved(b):
                return d
            # find empty
            empty = []
            for y in range(2):
                for x in range(3):
                    if b[y][x] == 0: empty = [y, x]
            
            moves = [
                [empty[0] - 1, empty[1]], # N
                [empty[0] + 1, empty[1]], # S
                [empty[0], empty[1] - 1], # W
                [empty[0], empty[1] + 1], # E
            ]

            for m in moves:
                if 0 <= m[0] < 2 and 0 <= m[1] < 3:
                    newboard = copy.deepcopy(b)
                    newboard[m[0]][m[1]], newboard[empty[0]][empty[1]] = newboard[empty[0]][empty[1]], newboard[m[0]][m[1]]
                    nbt = (tuple(newboard[0]), tuple(newboard[1])) # newboard tuple
                    if nbt in seen:
                        continue
                    else:
                        queue.append((newboard, d + 1))
                        seen.add(nbt)
        return -1