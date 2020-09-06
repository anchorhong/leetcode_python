class Solution:
    def max_product(self, nums):
        res = [[[float("-inf") for _ in range(2)] for _ in range(len(nums))] for
               _ in range(len(nums))]
        for i in range(len(nums)):
            res[i][i][1] = nums[i]

        max_value = float("-inf")
        for l in range(2, len(nums) + 1):
            for i in range(len(nums) - l + 1):
                j = i + l - 1
                res[i][j][0] = max(res[i][j - 1][0], res[i][j - 1][1],
                                   res[i + 1][j][0], res[i + 1][j][1])
                res[i][j][1] = res[i][j - 1][1] * nums[j]

                max_value = max(res[i][j][0], res[i][j][1], max_value)
        return max_value


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    print(Solution().max_product(nums))
