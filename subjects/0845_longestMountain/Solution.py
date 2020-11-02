from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        dp1 = [0] * len(A)
        dp2 = [0] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                dp1[i] = dp1[i - 1] + 1 if dp1[i - 1] != 0 else 2
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                dp2[i] = dp2[i + 1] + 1 if dp2[i + 1] != 0 else 2
        max = 0
        for i in range(len(A)):
            if dp1[i] and dp2[i]:
                max = max(dp1[i] + dp2[i] - 1, max)

        return max

if __name__ == "__main__":
    nums = [2, 1, 4, 7, 3, 2, 5]
    print(Solution().longestMountain(nums))
