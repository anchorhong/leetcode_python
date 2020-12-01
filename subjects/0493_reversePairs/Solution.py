from typing import List
from collections import defaultdict
import bisect


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    count += 1
        return count


if __name__ == "__main__":
    nums = [1, 3, 2, 3, 1]
    print(Solution().reversePairs(nums))
