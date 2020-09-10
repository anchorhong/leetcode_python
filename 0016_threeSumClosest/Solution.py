# https://leetcode-cn.com/problems/3sum-closest/
from typing import List
import math


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_sum, min_diff, nums_len = float('inf'), float('inf'), len(nums)
        list.sort(nums)
        for i in range(nums_len - 2):
            a, b_idx, c_idx = nums[i], i + 1, nums_len - 1
            while b_idx < c_idx:
                abc_sum = a + nums[b_idx] + nums[c_idx]
                diff = int(math.fabs(abc_sum - target))
                if diff < min_diff:
                    min_diff, min_sum = diff, abc_sum
                if abc_sum > target:
                    c_idx = c_idx - 1
                else:
                    b_idx = b_idx + 1

        return min_sum


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    print(Solution().threeSumClosest(nums, target))
