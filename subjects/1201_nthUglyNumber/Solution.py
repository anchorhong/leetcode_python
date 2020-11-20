import collections


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        nums = a * b + b * c + a * c - a - b - c
        n = n % nums
        cache = collections.defaultdict(int)
        pre, i = float('inf'), min(a, b, c)
        while i <= nums:
            cache