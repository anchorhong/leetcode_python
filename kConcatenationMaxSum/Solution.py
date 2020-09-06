import math


class Solution:
    def kConcatenationMaxSum(self, arr, k: int) -> int:
        maxs, s = 0, 0
        for a in (arr * min(2, k)):
            s = s + a
            if s < 0:
                s = 0
            if s > maxs:
                maxs = s

        if k <= 2:
            return maxs

        return (max(sum(arr), 0) * (k - 2) + maxs) % (10 ** 9 + 7)


if __name__ == '__main__':
    # arr = [1, 2]
    # k = 3
    # print(Solution().kConcatenationMaxSum(arr, k))
    # arr = [1, -2, 1]
    # k = 5
    # print(Solution().kConcatenationMaxSum(arr, k))
    arr = [4, 19, -6, 1, 17, 12, 3, -8, 6, 8, 18, 13, 2, -12, 18, -12, -14, 4,
           11]
    k = 16
    print(Solution().kConcatenationMaxSum(arr, k))
