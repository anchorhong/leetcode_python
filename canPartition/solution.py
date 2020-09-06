class Solution():
    def canPartition(self, nums):
        if sum(nums) % 2 != 0:
            return False
        res = []
        pre_res = []
        for n in nums:
            if n == sum(nums) / 2:
                return True
            res.append(n)
            if pre_res:
                for i in pre_res:
                    tmp = n + i
                    if tmp == sum(nums) / 2:
                        return True
                    res.append(tmp)
            pre_res = res
            res = list(pre_res)
        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 5]
    print(Solution().canPartition(nums))
