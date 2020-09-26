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


if __name__ == "__main__":
    nums = [-3, -2, -1, 0, 0, 1, 2, 3]
    target = 0
    print(Solution().fourSum(nums, target))
