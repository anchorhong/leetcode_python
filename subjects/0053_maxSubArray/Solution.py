from typing import List


class Solution:
    def max_sub_array_n(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pre, max_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if pre >= 0:
                max_sum = pre + nums[i] if  pre + nums[i] > max_sum else max_sum
                pre = pre + nums[i]
            else:
                max_sum = max(max_sum, nums[i])
                pre = nums[i]
        return max_sum


if __name__ == "__main__":
    nums = [1, -2, 0]
    print(Solution().maxSubArray(nums))
