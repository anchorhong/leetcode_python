from typing import List
from collections import Counter
from collections import defaultdict


# 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter = defaultdict(dict)
        for word in strs:
            counter[word] = Counter(word)

        dp = [[[0] * n for _ in range(m)] for _ in range(len(strs))]
        if counter[strs[0]][0] <= m and counter[strs[0]][1] <= n:
            dp[0][counter[strs[0]]['0'] - 1][counter[strs[0]]['1'] - 1] = 1
        for i in range(1, len(strs)):
            c_0, c_1 = counter[strs[i]]['0'], counter[strs[i]]['1']
            for j in range(len(dp[i - 1])):
                for k in range(len(dp[i - 1][j])):
                    if j >= c_0 and k >= c_1:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - c_0][k - c_1] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
        print(dp)
        return max(map())


if __name__ == "__main__":
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    print(Solution().findMaxForm(strs, m, n))
