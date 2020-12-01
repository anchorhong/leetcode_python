from typing import List
from collections import defaultdict


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        def calculate_max_gap(nums: List[int]) -> int:
            m = 0
            for i in range(len(nums) - 1):
                if nums[i + 1] - nums[i] > m:
                    m = nums[i + 1] - nums[i]
            return m

        nums = set(nums)
        if len(nums) < 2:
            return 0

        bucket = defaultdict(list)
        min_num = min(nums)
        bucket_cap = (max(nums) - min(nums)) // len(nums)
        bucket_size = max(nums) // bucket_cap + 1
        for n in nums:
            bucket[(n - min_num) // bucket_cap].append(n)
        idxes = list()
        for i in range(bucket_size):
            if len(bucket[i]) != 0:
                idxes.append(i)
                bucket[i].sort()
        max_gap = 0
        for i in range(len(idxes)):
            if i == len(idxes) - 1:
                x = calculate_max_gap(bucket[idxes[i]])
            else:
                x_1 = calculate_max_gap(bucket[idxes[i]])
                x_2 = bucket[idxes[i + 1]][0] - bucket[idxes[i]][-1]
                x = max(x_1, x_2)
            if x > max_gap:
                max_gap = x

        return max_gap


if __name__ == "__main__":
    nums = [1, 1, 1, 1]
    print(Solution().maximumGap(nums))
