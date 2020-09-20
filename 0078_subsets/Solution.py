from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def dfs(sub: List[int], idx: int):
            if idx == len(nums):
                return
            select = sub.copy()
            select.append(nums[idx])
            r = select.copy()
            res.append(r)
            dfs(res, select, idx + 1)
            dfs(res, sub, idx + 1)

        dfs(res, list(), 0)
        return res

    def subsets_1(self, nums: List[int]) -> List[List[int]]:

        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(sub, idx):
            res.append(sub)
            for i in range(idx, len(nums)):
                dfs(sub + [nums[i]], i + 1)

        dfs([], 0)
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subsets_2(nums))
