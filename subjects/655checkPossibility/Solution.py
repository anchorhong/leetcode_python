class Solution:
    def checkPossibility(self, nums) -> bool:
        times = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if times == 0:
                    return False
                elif i - 2 >= 0:
                    if nums[i] >= nums[i - 2]:
                        nums[i - 1] = nums[i]
                    else:
                        nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
                times = 0
        return True


if __name__ == '__main__':
    # nums = [4, 2, 3]
    # print(Solution().checkPossibility(nums))
    # nums = [4, 2, 1]
    # print(Solution().checkPossibility(nums))
    nums = [1, 4, 1, 2]
    print(Solution().checkPossibility(nums))
