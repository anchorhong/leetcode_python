from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2
        list.sort(nums, reverse=True)

        def dfs(nums: List[int], idx: int, t: int) -> bool:
            if t == 0:
                return True
            if idx == len(nums) or nums[idx] > t:
                return
            if dfs(nums, idx + 1, t - nums[idx]):
                return True
            if dfs(nums, idx + 1, t):
                return True

        if dfs(nums, 0, target):
            return True
        return False


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 100]
    print(Solution().canPartition(nums))
