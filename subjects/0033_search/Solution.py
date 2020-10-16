from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                is_left = int(nums[left] > nums[mid])
                if not is_left and target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif target > nums[mid]:
                is_left = int(nums[left] > nums[mid])
                if is_left and target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(Solution().search(nums, target))
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    print(Solution().search(nums, target))
    nums = [1]
    target = 0
    print(Solution().search(nums, target))
    nums = [5, 1, 3]
    target = 5
    print(Solution().search(nums, target))
    nums = [3, 5, 1]
    target = 3
    print(Solution().search(nums, target))
    nums = [4, 5, 6, 7, 8, 1, 2, 3]
    target = 8
    print(Solution().search(nums, target))
