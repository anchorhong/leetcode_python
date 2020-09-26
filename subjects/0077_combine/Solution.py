# https://leetcode-cn.com/problems/combinations/
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return list()
        res = [[i] for i in range(1, n - k + 2)]
        tmp = list()
        for tk in range(k - 1, 0, -1):
            for lst in res:
                for x in range(lst[-1] + 1, n - tk + 2):
                    new_list = lst[:]
                    new_list.append(x)
                    tmp.append(new_list)
            res = tmp
            tmp = list()
        return res


if __name__ == "__main__":
    print(Solution().combine(4, 2))