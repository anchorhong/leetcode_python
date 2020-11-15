from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        s, n = 0, len(nums)
        sums = [sum(nums[:i + 1]) for i in range(n)]

        def count_range_sum(left, right):
            if left == right:
                return 0
            else:
                mid = (left + right) // 2
                n1 = count_range_sum(left, mid)
                n2 = count_range_sum(mid + 1, right)
                ret = n1 + n2

                l, r = mid + 1, mid + 1
                for i in range(left, mid + 1):
                    while l <= right and sums[l] - sums[i] < lower:
                        l += 1
                    while r <= right and sums[r] - sums[i] > upper:
                        r += 1
                    ret += r - l + 1
                sorted = [float('inf')] * (right - left + 1)
                p1, p2 = left, mid + 1
                p0 = 0
                while p1 <= mid or p2 <= right:
                    if p1 > mid:
                        sorted[p0] = sums[p2]
                        p2 += 1
                    elif p2 > right:
                        sorted[p0] = sums[p1]
                        p1 += 1
                    else:
                        if sums[p1] < sums[p2]:
                            sorted[p0] = sums[p1]
                            p1 += 1
                        else:
                            sorted[p0] = sums[p2]
                            p2 += 1
                    p0 += 1
                sums[left:left + len(sorted)] = sorted[:]
                return ret

        return count_range_sum(0, len(nums) - 1)


if __name__ == "__main__":
    nums = [-2, 5, -1]
    lower = -2
    upper = 2
    print(Solution().countRangeSum(nums, lower, upper))
