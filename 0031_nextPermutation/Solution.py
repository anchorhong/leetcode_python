from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                j, k = i, len(nums) - 1
                while k >= j:
                    if nums[k] > nums[i - 1]:
                        break
                    k -= 1
                nums[i - 1], nums[k] = nums[k], nums[i - 1]
                start, end = j, len(nums) - 1
                while start < end:
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                    end -= 1
                break
            i -= 1
        if i == 0:
            nums.reverse()
        return nums


if __name__ == "__main__":
    print(Solution().nextPermutation([1, 1, 2, 5]))
    print(Solution().nextPermutation([1, 2, 3]))
    print(Solution().nextPermutation([3, 2, 1]))
    print(Solution().nextPermutation([1, 1, 5]))
    print(Solution().nextPermutation([1, 3, 2]))
    print(Solution().nextPermutation([1, 2]))
