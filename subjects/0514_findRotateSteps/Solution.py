# 输入: ring = "godding", key = "gd"
# 输出: 4
from collections import defaultdict
import math


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        words = defaultdict(list)
        for i in range(len(ring)):
            words[ring[i]].append(i)
        dp = defaultdict(int)
        for idx in words[key[0]]:
            dp[idx] = min(idx - 0, n - idx) + 1
        for i in range(1, len(key)):
            tmp = defaultdict(int)
            for idx in words[key[i]]:
                min_dist = float('inf')
                for j in dp.keys():
                    dis2 = n - j + idx if j > idx else n - idx + j
                    dist = min(int(math.fabs(idx - j)), dis2) + 1  + dp[j]
                    if dist < min_dist:
                        min_dist = dist
                tmp[idx] = min_dist
            dp = tmp
        return min(dp.values())


if __name__ == "__main__":
    ring = "godding"
    key = "gd"
    print(Solution().findRotateSteps(ring, key))
