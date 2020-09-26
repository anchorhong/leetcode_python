# https://leetcode-cn.com/problems/max-consecutive-ones/
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c_max, c_tmp = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c_tmp = c_tmp + 1 if i > 0 and nums[i - 1] == 1 else 1
                if i == len(nums) - 1 and c_tmp > c_max:
                    c_max = c_tmp
            elif c_tmp > c_max:
                c_max = c_tmp
                c_tmp = 0
        return c_max
