import math


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:

        for i in range(len(nums) - 1):
            for j in range(i + 1, min(len(nums), i + k + 1)):
                if math.fabs(nums[i] - nums[j]) <= t:
                    return True

        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(Solution().containsNearbyAlmostDuplicate(nums, 3, 0))
    nums = [1, 0, 1, 1]
    print(Solution().containsNearbyAlmostDuplicate(nums, 1, 2))
    nums = [1, 5, 9, 1, 5, 9]
    print(Solution().containsNearbyAlmostDuplicate(nums, 2, 3))
