from typing import List
from typing import Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = list()

        def dfs(num_set: Set[int], combine: List[int]):
            nonlocal res
            if len(num_set) == 0:
                res.append(combine)
            for num in num_set:
                tmp_set, tmp_combine = num_set.copy(), combine.copy()
                tmp_set.remove(num)
                tmp_combine.append(num)
                dfs(tmp_set, tmp_combine)

        dfs(set(nums), [])
        return res
