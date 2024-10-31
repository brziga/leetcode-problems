# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [set() for i in range(n)] # rows
        cols = [set() for i in range(n)] # columns
        subs = [[set() for i in range(3)] for i in range(3)] # subsquares

        for y in range(n):
            for x in range(n):
                num = board[y][x]
                if num == '.': continue

                if num in rows[y]:
                    # print(y, x, num, "rows")
                    return False
                else:
                    rows[y].add(num)
                
                if num in cols[x]:
                    # print(y, x, num, "cols")
                    return False
                else:
                    cols[x].add(num)
                
                if num in subs[y//3][x//3]:
                    # print(y, x, num, "subs")
                    return False
                else:
                    subs[y//3][x//3].add(num)
        
        return True