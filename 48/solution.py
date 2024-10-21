# https://leetcode.com/problems/rotate-image/description/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # transpose matrix in-place
        y, x = 0, 1
        while y < len(matrix):
            for i in range(x, len(matrix[0])):
                temp = matrix[y][i]
                matrix[y][i] = matrix[i][y]
                matrix[i][y] = temp
            x += 1
            y += 1
        
        # reverse lines in matrix
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]