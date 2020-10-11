from typing import List


class Solution:
    def sort_colors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        r, w, b = 0, 0, len(nums)
        while w < b:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
            elif nums[w] == 2:
                b -= 1
                nums[b], nums[w] = nums[w], nums[b]
            else:
                w += 1
