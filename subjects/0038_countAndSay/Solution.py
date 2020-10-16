# https://leetcode-cn.com/problems/count-and-say/


class Solution:
    @staticmethod
    def count_and_say(n: int) -> str:
        def say(strs: str) -> str:
            times, res, pre = 0, "", None
            for s in strs:
                if pre and s != pre:
                    res += str(times) + pre
                    times = 1
                else:
                    times += 1
                pre = s
            if times != 0:
                res += str(times) + pre
            return res

        result = "1"
        for i in range(1, n):
            result = say(result)
        return result
