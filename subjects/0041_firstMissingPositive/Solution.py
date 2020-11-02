from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] - 1 != i and nums[i] - 1 < len(
                    nums) and nums[nums[i] - 1] - 1 != nums[i] - 1:
                tmp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp
        for i in range(len(nums)):
            if nums[i] <= 0 or i != nums[i] - 1:
                return i + 1
        return max(nums) + 1 if nums and max(nums) >= 0 else 1


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1, 2]
    print(Solution().firstMissingPositive(nums))
