class Solution:
    def twoSum(self, nums, target: int):
        s = {}
        res = []
        for i in range(len(nums)):
            s[target - nums[i]] = i
        for i in range(len(nums)):
            j = s.get(nums[i])
            if j and j != i:
                res.append(i)
                res.append(j)
                return res
        return res


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    print(Solution().twoSum(nums, 9))
