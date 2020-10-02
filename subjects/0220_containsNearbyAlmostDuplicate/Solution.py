from typing import List
import math


class Solution:
    @staticmethod
    def contains_nearby_almost_duplicate(nums: List[int], k: int,
                                         t: int) -> bool:
        for i in range(len(nums)):
            for j in range(max(i - k, 0), i):
                if int(math.fabs(nums[i] - nums[j])) <= t:
                    return True

    @staticmethod
    def contains_nearby_almost_duplicate(nums: List[int], k: int,
                                         t: int) -> bool:
        if k == 0:
            return False
        bucket = dict()
        for i in range(len(nums)):
            bucket_id = math.floor(nums[i] / t + 1)
            if bucket.get(bucket_id) is not None:
                return True
            if bucket.get(bucket_id - 1) is not None and int(
                    math.fabs(bucket.get(bucket_id - 1) - nums[i])) <= t:
                return True
            if bucket.get(bucket_id + 1) is not None and int(
                    math.fabs(bucket.get(bucket_id + 1) - nums[i])) <= t:
                return True
            if len(bucket.keys()) == k:
                del bucket[math.floor(nums[i - k] / (t + 1))]
            bucket[bucket_id] = nums[i]
        return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int,
                                      t: int) -> bool:
        for i in range(len(nums) - 1):
            j_max = min(i + k + 1, len(nums))
            for j in range(i + 1, j_max):
                if int(math.fabs(nums[i] - nums[j])) <= t:
                    return True

        return False
