# https://leetcode-cn.com/problems/contains-duplicate-ii/

from typing import List
import math


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx_dict = dict()
        for i in range(len(nums)):
            if nums[i] in idx_dict and int(
                    math.fabs(idx_dict.get(nums[i]) - i)) <= k:
                return True
            else:
                idx_dict[nums[i]] = i

        return False
