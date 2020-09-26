from typing import List
from typing import Set
from typing import Dict
import math


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        bucket = [[dict() for _ in range(3)] for _ in range(3)]
        row_dict = [dict() for _ in range(len(board))]
        col_dict = [dict() for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    row_dict[i][str(board[i][j])] = False
                    col_dict[j][str(board[i][j])] = False
                    bucket[math.floor(i / 3)][math.floor(j / 3)][str(board[i][j])] = False

        def dfs(board, bucket, row_dict, col_dict, row, col, result) -> bool:
            if row == len(board):
                result.append(board.copy())
                return True
            if col == len(board):
                return dfs(board, bucket, row_dict, col_dict, row + 1, 0, result)
            elif board[row][col] != ".":
                return dfs(board, bucket, row_dict, col_dict, row, col + 1, result)
            else:
                available = set([str(k) for k in range(1, 10)]) - set(row_dict[row].keys()) - set(
                    col_dict[col].keys()) - set(bucket[math.floor(row / 3)][math.floor(col / 3)].keys())
                for x in available:
                    row_dict[row][str(x)] = True
                    col_dict[col][str(x)] = True
                    bucket[math.floor(row / 3)][math.floor(col / 3)][str(x)] = True
                    board[row][col] = x
                    if dfs(board, bucket, row_dict, col_dict, row, col + 1, result):
                        return True
                    board[row][col] = "."
                    if row_dict[row][str(x)]:
                        del row_dict[row][str(x)]
                    if col_dict[col][str(x)]:
                        del col_dict[col][str(x)]
                    if bucket[math.floor(row / 3)][math.floor(col / 3)][str(x)]:
                        del bucket[math.floor(row / 3)][math.floor(col / 3)][str(x)]
                return False

        result = list()
        dfs(board, bucket, row_dict, col_dict, 0, 0, result)
        for i in range(len(board)):
            for j in range(len(board)):
                board[i][j] = result[0][i][j]


if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    Solution().solveSudoku(board)
    print(board)
