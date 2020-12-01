from typing import List


class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     i , j = 0, len(nums) - 1
    #     start, end = None, None
    #     while i <= j:
    #         if nums[i] != target:
    #             i += 1
    #         elif nums[i] == target and start is None:
    #             start = i
    #         if nums[j] != target:
    #             j -= 1
    #         elif nums[j] == target and end is None:
    #             end = j
    #         if start is not None  and end is not None:
    #             return [start, end]
    #     return [-1, -1]
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start, end = mid - 1, mid + 1
                while start >=0 and nums[start] == target:
                    start -= 1
                while end <= len(nums) - 1 and nums[end] == target:
                    end += 1
                return [start + 1, end - 1]
        return [-1, -1]


if __name__ == "__main__":
    nums = [2, 2]
    target = 2
    print(Solution().searchRange(nums, target))
