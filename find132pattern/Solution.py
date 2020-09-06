class Solution:
    def find132pattern(self, nums):
        if len(nums) < 3:
            return False
        min_idx = 0
        max_idx = -1

        for i in range(1, len(nums)):
            if nums[i] <= nums[min_idx] and i == min_idx + 1:
                min_idx = i
            if nums[i] > nums[min_idx]:
                max_idx = i


if __name__ == '__main__':
    # nums = [1, 2, 3, 4]
    # print(Solution().find132pattern(nums))
    # nums = [3, 1, 4, 2]
    # print(Solution().find132pattern(nums))
    # nums = [-1, 3, 2, 0]
    # print(Solution().find132pattern(nums))
    nums = [8, 10, 4, 6, 5]
    print(Solution().find132pattern(nums))
    nums = [3, 5, 0, 3, 4]
    print(Solution().find132pattern(nums))
