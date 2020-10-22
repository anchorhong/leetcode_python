from typing import List


class Solution:
    def total_n_queens(self, n: int) -> int:
        res = 0
        def is_valid(row, col, board: List[List[bool]]) -> bool:
            if any(board[row]) or any([b[col] for b in board]):
                return False
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j]:
                    return False
                i -= 1
                j -= 1
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j]:
                    return False
                i -= 1
                j += 1
            return True

        def dfs(row: int, col: int, board: List[List]):
            nonlocal res
            if col == n:
                row, col = row + 1, 0
                if row == n:
                    if all([any(b) for b in board]):
                        res += 1
                    return
            pre = board[row][col]
            if is_valid(row, col, board):
                board[row][col] = True
                dfs(row, col + 1, board)
            board[row][col] = pre
            dfs(row, col + 1, board)

        board = [[False] * n for _ in range(n)]
        dfs(0, 0, board)
        return res


if __name__ == "__main__":
    print(Solution().total_n_queens(4))
