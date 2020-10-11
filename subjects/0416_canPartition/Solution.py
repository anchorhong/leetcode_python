from typing import List


class Solution:
    # @staticmethod
    # def can_partition(nums: List[int]) -> bool:
    #     if sum(nums) % 2 != 0:
    #         return False
    #     list.sort(nums, reverse=True)
    #
    #     def dfs(idx: int, t: int) -> bool:
    #         if t == 0:
    #             return True
    #         if idx == len(nums) or nums[-1] > t:
    #             return
    #         if nums[idx] > t:
    #             if dfs(idx + 1, t):
    #                 return True
    #         else:
    #             if dfs(idx + 1, t - nums[idx]):
    #                 return True
    #             if dfs(idx + 1, t):
    #                 return True
    #
    #     return True if dfs(0, sum(nums) // 2) else False

    @staticmethod
    def can_partition(nums: List[int]) -> bool:
        if sum(nums) % 2 != 0 or len(nums) < 2:
            return False
        target = sum(nums) // 2
        if max(nums) > target:
            return False

        dp = [[False] * (target + 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1, len(nums)):
            for j in range(1, target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(nums) - 1][-1]


if __name__ == "__main__":
    n = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
         100, 100, 99, 97]
    print(Solution.can_partition(n))
