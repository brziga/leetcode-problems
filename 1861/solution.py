# https://leetcode.com/problems/rotating-the-box/

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])

        # "sink" stones
        for c in range(m):
            col = box[c]
            i = n - 1
            s = 0
            while i >= 0:
                if col[i] == "*":
                    s = 0
                elif col[i] == "#":
                    if s > 0:
                        col[i], col[i + s] = col[i + s], col[i]
                        i += s
                    s = 0
                else:
                    s += 1
                i -= 1

        # rotate matrix (box)
        rbox = [[' '] * m for _ in range(n)] # rotated box
        for i in range(m):
            for j in range(n):
                rbox[j][i] = box[i][j]
        for i in range(n):
            rbox[i] = rbox[i][::-1]
        
        return rbox