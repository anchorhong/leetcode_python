# https://leetcode-cn.com/problems/combination-sum-iii/
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res, combine, start = list(), list(), 1
        self.__dfs(n, k, start, combine, res)
        return res

    def __dfs(self, target: int, k: int, cur: int, combine: List[int],
              res: List[List[int]]):
        if k == 0 and target == 0:
            res.append(combine)
        elif k == 0 and target != 0:
            return
        elif target < 0 or cur > 9:
            return
        else:
            tmp_combine = combine.copy()
            tmp_combine.append(cur)
            self.__dfs(target - cur, k - 1, cur + 1, tmp_combine, res)
            self.__dfs(target, k, cur + 1, combine, res)


if __name__ == "__main__":
    k = 3
    n = 7
    print(Solution().combinationSum3(k, n))
    k = 3
    n = 9
    print(Solution().combinationSum3(k, n))