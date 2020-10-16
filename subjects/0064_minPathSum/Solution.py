# https://leetcode-cn.com/problems/minimum-path-sum/
from typing import List


class Solution:
    def min_path_sum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]

    def min_path_sum_opt_space(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [float('inf') for _ in range(n)]
        for i in range(0, m):
            left = float('inf')
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif i == 0 and j != 0:
                    dp[j] = dp[j - 1] + grid[i][j]
                elif j == 0 and i != 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], left) + grid[i][j]
                left = dp[j]
        return dp[n - 1]


if __name__ == "__main__":
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]

    print(Solution().min_path_sum_opt_space(grid))
    print(Solution().min_path_sum(grid))
