# 请你帮忙设计一个程序，用来找出第 n 个丑数。
#
# 丑数是可以被 a 或 b 或 c 整除的 正整数。

# 示例 1：
#
# 输入：n = 3, a = 2, b = 3, c = 5
# 输出：4
# 解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
# 示例 2：
#
# 输入：n = 4, a = 2, b = 3, c = 4
# 输出：6
# 解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。
# 示例 3：
#
# 输入：n = 5, a = 2, b = 11, c = 13
# 输出：10
# 解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
# 示例 4：
#
# 输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
# 输出：1999999984


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        a1, b1, c1 = a, b, c
        minx = min(a1, b1, c1)
        i = 1
        while i < n:
            t = min(a1, b1, c1)
            if t == a1:
                a1 = a1 + a
            elif t == b1:
                b1 = b1 + b
            else:
                c1 = c1 + c
            if t > minx:
                i += 1
                minx = t
        return minx


if __name__ == '__main__':
    print(Solution().nthUglyNumber(3, 2, 3, 5))
    print(Solution().nthUglyNumber(4, 2, 3, 4))
    print(Solution().nthUglyNumber(5, 2, 11, 13))
    print(Solution().nthUglyNumber(1000000000, 2, 217983653, 336916467))
