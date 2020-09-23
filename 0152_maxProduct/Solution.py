from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mx, mi, result = 1, 1, None
        for num in nums:
            if num == 0:
                mx, mi = 1, 1
                if result is None:
                    result = 0
            tmp = mx * num
            mx = max(tmp, num, mi * num)
            mi = min(tmp, num, mi * num)
            if result is None or mx > result:
                result = mx
        return result


if __name__ == "__main__":
    nums = [-2, 0, -1]
    print(Solution().maxProduct(nums))
