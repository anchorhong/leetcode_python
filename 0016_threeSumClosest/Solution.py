# https://leetcode-cn.com/problems/3sum-closest/
from typing import List
import math


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = [float('inf'), float('inf')]
        self.__dfs(nums, target, 0, 0, 3, res)
        return res[0]

    def __dfs(self, nums: List[int], target: int, sum: int, idx: int, n: int,
              res: List[int]):
        if n == 0:
            if int(math.fabs(sum - target)) < res[-1]:
                minx = int(math.fabs(sum - target))
                res[-1] = minx
                res[0] = sum
        if idx == len(nums):
            return

        self.__dfs(nums, target, sum + nums[idx], idx + 1, n - 1, res)
        self.__dfs(nums, target, sum, idx + 1, n, res)


if __name__ == "__main__":
    nums = [13,2,0,-14,-20,19,8,-5,-13,-3,20,15,20,5,13,14,-17,-7,12,-6,0,20,-19,-1,-15,-2,8,-2,-9,13,0,-3,-18,-9,-9,-19,17,-14,-19,-4,-16,2,0,9,5,-7,-4,20,18,9,0,12,-1,10,-17,-11,16,-13,-14,-3,0,2,-18,2,8,20,-15,3,-13,-12,-2,-19,11,11,-10,1,1,-10,-2,12,0,17,-19,-7,8,-19,-17,5,-5,-10,8,0,-12,4,19,2,0,12,14,-9,15,7,0,-16,-5,16,-12,0,2,-16,14,18,12,13,5,0,5,6]
    sorted(nums)
    target = -59
    print(Solution().threeSumClosest(nums, target))
