# https://leetcode-cn.com/problems/combination-sum/
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[
        List[int]]:
        res = []
        combine = []
        self.dfs(res, combine, candidates, target, 0)
        return res

    def dfs(self, res: List[List[int]], combine: List[int],
            candidates: List[int], target: int, idx: int):
        if idx == len(candidates):
            return
        if target == 0:
            res.append(combine)
            return
        elif target > 0:
            tmp = combine.copy()
            tmp.append(candidates[idx])
            self.dfs(res, tmp, candidates, target - candidates[idx], idx)
            self.dfs(res, combine, candidates, target, idx + 1)
        else:
            return


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))
    candidates = [2, 3, 5]
    target = 8
    print(Solution().combinationSum(candidates, target))
