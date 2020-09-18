from typing import List
from collections import defaultdict


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result_set, n, num_dict = set(), len(nums), defaultdict(int)
        for num in nums:
            num_dict[num] += 1

        def dfs(available, combine: List[int]):
            if len(combine) == n and tuple(combine) not in result_set:
                result_set.add(tuple(combine))
                return
            keys = list(available.keys())
            for x in keys:
                tmp = combine.copy()
                tmp.append(x)
                available[x] -= 1
                if available[x] == 0:
                    del available[x]
                dfs(available, tmp)
                available[x] += 1

        dfs(num_dict, list())
        return [list(t) for t in result_set]


if __name__ == "__main__":
    print(Solution().permuteUnique([1, 1, 2]))
