# https://leetcode-cn.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_capacity = 0
        while left < right:
            capacity = (right - left) * min(height[right], height[left])
            if capacity > max_capacity:
                max_capacity = capacity
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_capacity
