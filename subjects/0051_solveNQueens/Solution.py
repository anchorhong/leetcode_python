from typing import List
import copy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def is_valid(i: int, j: int, board: List[str]) -> bool:
            if "Q" in board[i] or "Q" in [board[k][j] for k in range(i)]:
                return False
            r, c = i - 1, j - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r, c = r - 1, c - 1
            r, c = i - 1, j + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r, c = r - 1, c + 1
            return True

        res = list()

        def dfs(i: int, j: int, board: List[List[str]]):
            if i == n:
                if all(["Q" in b for b in board]):
                    tmp = copy.deepcopy(board)
                    res.append(tmp)
                return
            if j == n:
                dfs(i + 1, 0, board)
            else:
                if is_valid(i, j, board):
                    board[i][j] = "Q"
                    dfs(i, j + 1, board)
                board[i][j] = "."
                dfs(i, j + 1, board)

        board = [["."] * n for _ in range(n)]
        dfs(0, 0, board)

        return [["".join(row) for row in r] for r in res]


if __name__ == "__main__":
    print(Solution().solveNQueens(10))
