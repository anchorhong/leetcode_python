class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) < 2:
            return len(nums)
        prediff = nums[1] - nums[0]
        ret = 2 if prediff != 0 else 1

        for i in range(2, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff > 0 >= prediff or diff < 0 <= prediff:
                ret += 1
                prediff = diff
        return ret


if __name__ == '__main__':
    nums = [33, 53, 12, 64, 50, 41, 45, 21, 97, 35, 47, 92, 39, 0, 93, 55, 40, 46, 69, 42, 6, 95, 51, 68, 72, 9, 32, 84,
            34, 64, 6, 2, 26, 98, 3, 43, 30, 60, 3, 68, 82, 9, 97, 19, 27, 98, 99, 4, 30, 96, 37, 9, 78, 43, 64, 4, 65,
            30, 84, 90, 87, 64, 18, 50, 60, 1, 40, 32, 48, 50, 76, 100, 57, 29, 63, 53, 46, 57, 93, 98, 42, 80, 82, 9,
            41, 55, 69, 84, 82, 79, 30, 79, 18, 97, 67, 23, 52, 38, 74, 15]
    print(Solution().wiggleMaxLength(nums))