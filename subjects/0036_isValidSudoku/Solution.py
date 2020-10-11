from typing import List


class Solution:
    @staticmethod
    def is_valid_sudoku(board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(len(board))]
        column_set = [set() for _ in range(len(board))]
        boards = list()
        for i in range(len(board)):
            if i % 3 == 0:
                boards = [set(), set(), set()]
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in row_set[i] or board[i][j] in column_set[
                    j] or board[i][j] in boards[j // 3]:
                    return False
                else:
                    row_set[i].add(board[i][j])
                    column_set[j].add(board[i][j])
                    boards[j // 3].add(board[i][j])
        return True
