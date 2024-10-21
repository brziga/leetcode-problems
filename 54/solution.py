# https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = [0, len(matrix) - 1]  # row index limits
        cols = [0, len(matrix[0]) - 1]  # column index limits
        mode = [0, 1]  # change value for row and col index
        r, c = 0, 0
        out = []
        count = len(matrix) * len(matrix[0])
        while len(out) < count:
            out.append(matrix[r][c])
            if r == rows[0] and mode[0] < 0:
                cols[0] += 1
                mode[1] = -mode[0]
                mode[0] = 0
            elif r == rows[1] and mode[0] > 0:
                cols[1] -= 1
                mode[1] = -mode[0]
                mode[0] = 0
            elif c == cols[0] and mode[1] < 0:
                rows[1] -= 1
                mode[0] = mode[1]
                mode[1] = 0
            elif c == cols[1] and mode[1] > 0:
                rows[0] += 1
                mode[0] = mode[1]
                mode[1] = 0
            r += mode[0]
            c += mode[1]
        return out
