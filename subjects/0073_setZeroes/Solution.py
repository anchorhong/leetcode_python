from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix[i])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = float('-inf')
                    for m in matrix:
                        if m[j] != 0:
                            m[j] = float('-inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == float('-inf'):
                    matrix[i][j] = 0
