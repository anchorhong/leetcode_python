# https://leetcode-cn.com/problems/combination-sum-ii/
from typing import *


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[
        List[int]]:
        res_set, combine, res = set(), list(), list()
        list.sort(candidates)
        self.__dfs(candidates, target, 0, combine, res_set)
        for s in res_set:
            res.append(list(s))
        return res

    def __dfs(self, candidates: List[int], target: int, idx: int,
              combine: List[int], res: Set[Tuple[int]]):
        if target == 0:
            res.add(tuple(combine))
        elif idx == len(candidates) or target - candidates[idx] < 0:
            return
        else:
            tmp_combine = combine.copy()
            tmp_combine.append(candidates[idx])
            self.__dfs(candidates, target - candidates[idx], idx + 1,
                       tmp_combine, res)
            self.__dfs(candidates, target, idx + 1, combine, res)


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates, target))
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(Solution().combinationSum2(candidates, target))
