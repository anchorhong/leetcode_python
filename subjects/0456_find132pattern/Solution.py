class Solution:
    def find132pattern(self, nums):
        mi = [nums[0]]
        for i in range(1, len(nums)):
            mi.append(min(nums[i], mi[i - 1]))

        stack = []
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > mi[j]:
                while stack and stack[-1] <= mi[j]:
                    stack.pop()

                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])

        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().find132pattern(nums))
    nums = [3, 1, 4, 2]
    print(Solution().find132pattern(nums))
    nums = [-1, 3, 2, 0]
    print(Solution().find132pattern(nums))
    nums = [8, 10, 4, 6, 5]
    print(Solution().find132pattern(nums))
    nums = [3, 5, 0, 3, 4]
    print(Solution().find132pattern(nums))
