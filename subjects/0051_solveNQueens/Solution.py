from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = list()
        s0, s1, s2 = [False] * n, [False] * (2 * n - 1), [False] * (2 * n - 1)

        def dfs(r: int, board: List[List[str]]):
            if r == n:
                res.append(list(map(''.join, board)))
                return
            for c in range(n):
                if not (s0[c] or s1[n - 1 - r + c] or s2[r + c]):
                    board[r][c] = "Q"
                    s0[c], s1[n - 1 - r + c], s2[r + c] = True, True, True
                    dfs(r + 1, board)
                    board[r][c] = "."
                    s0[c], s1[n - 1 - r + c], s2[r + c] = False, False, False

        board = [["."] * n for _ in range(n)]
        dfs(0, board)
        return res


if __name__ == "__main__":
    res = Solution().solveNQueens(4)
    print(res)
