# https://leetcode.com/problems/maximum-matrix-sum/

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        min_ = 10e5
        num_of_negs = 0
        for y in range(n):
            for x in range(n):
                num = matrix[y][x]
                num_of_negs += 1 if num <= 0 else 0
                num = abs(num)
                min_ = num if num < min_ else min_
                matrix[y][x] = num
        mat_sum = sum([sum(row) for row in matrix])
        if num_of_negs % 2 == 0:
            return mat_sum
        else:
            return mat_sum - 2 * min_