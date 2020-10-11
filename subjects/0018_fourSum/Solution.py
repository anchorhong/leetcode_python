from typing import List
from collections import defaultdict


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        two_sum = [[nums[i] + nums[j] if j > i else float('inf') for j in
                    range(length)] for i in range(length)]
        complement_sum = [
            [target - two_sum[i][j] if j > i else float('inf') for j in
             range(length)] for i in range(length)]
        sum_dict = defaultdict(list)
        for i in range(length):
            for j in range(i + 1, length):
                sum_dict[two_sum[i][j]].append([i, j])

        res = set()
        for i in range(length - 3):
            for j in range(i + 1, len(complement_sum) - 2):
                index_list = sum_dict.get(complement_sum[i][j])
                if index_list:
                    for i_l in index_list:
                        if j < i_l[0]:
                            res.add((nums[i],
                                     nums[j], nums[i_l[0]], nums[i_l[1]]))
        res_list = list()
        for r in res:
            res_list.append(list(r))
        return res_list

    def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = dict()

        def dfs(nums: List[int], combine: List[int], idx: int, s: int):
            if s == target and len(combine) == 4 and tuple(combine) not in res:
                res[tuple(combine)] = combine
            if len(combine) >= 4 or idx == len(nums):
                return
            tmp = combine.copy()
            tmp.append(nums[idx])
            dfs(nums, tmp, idx + 1, s + nums[idx])
            dfs(nums, combine, idx + 1, s)

        dfs(nums, list(), 0, 0)
        return list(res.values())


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    target = -1
    print(Solution().four_sum(nums, target))
