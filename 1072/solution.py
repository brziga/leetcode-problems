# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = {}
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            row = tuple(matrix[i])
            negrow = matrix[i].copy()
            for j in range(c):
                negrow[j] = 0 if negrow[j] == 1 else 1
            negrow = tuple(negrow)
            if row in patterns:
                patterns[row] += 1
            elif negrow in patterns:
                patterns[negrow] += 1
            else:
                patterns[row] = 1
        mc = sorted(patterns.items(), key = lambda x: x[1], reverse = True)[0]
        return mc[1]