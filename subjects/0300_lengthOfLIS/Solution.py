from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = 1
        for i in range(1, n):
            maxx = 0
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j] and dp[j] > maxx:
                    maxx = dp[j]
            dp[i] = maxx + 1
        return max(dp)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().lengthOfLIS(nums))
