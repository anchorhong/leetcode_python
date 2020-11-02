from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set, res = set(wordDict), list()

        def dfs(pre: int, cur: int, combine: list):
            if cur == len(s):
                if pre == cur and len(combine) != 0:
                    res.append(combine)
                return
            if s[pre: cur + 1] in word_set:
                tmp = combine.copy()
                tmp.append(s[pre:cur + 1])
                dfs(cur + 1, cur + 1, tmp)
            dfs(pre, cur + 1, combine)

        dfs(0, 0, list())
        result = list()
        for c in res:
            result.append(' '.join(c))
        return result

    def word_break(self, s: str, wordDict: List[str]) -> List[str]:
        n, words = len(s), set(wordDict)
        dp = [False] * n
        lens = set(map(len, wordDict))
        for i in range(n):
            for l in lens:
                if i == 0 and i + l <= n and s[i:i + l] in words:
                    dp[i + l - 1] = True
                elif i + l <= n and i - 1 >= 0 and s[i:i + l] in words:
                    dp[i + l - 1] = dp[i + l - 1] or dp[i - 1]
        res, result = list(), list()

        def dfs(dp: List[bool], row: int, combine: list):
            if row < 0:
                res.append(combine)
                return
            if not dp[row]:
                return
            for w in words:
                if s[row - len(w) + 1:row + 1] == w:
                    tmp = combine.copy()
                    tmp.append(w)
                    dfs(dp, row - len(w), tmp)

        dfs(dp, n - 1, list())
        for c in res:
            result.append(' '.join(reversed(c)))
        return result

    def word_break_backtrack(self, s: str, wordDict: List[str]) -> List[str]:
        res, words = list(), set(wordDict)
        mem = [1] * (len(s) + 1)

        def dfs(pos: int, combine: List[str]):
            num = len(res)
            if pos == len(s):
                res.append(" ".join(combine))
                return
            for i in range(pos, len(s) + 1):
                if mem[i] and s[pos:i] in words:
                    combine.append(s[pos:i])
                    dfs(i, combine)
                    combine.pop()
            mem[pos] = 1 if len(res) > num else 0

        dfs(0, list())
        return res


if __name__ == "__main__":
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa",
                "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

    # s = "catsanddog"
    # wordDict = ["cat", "cats", "and", "sand", "dog"]
    # s = "goalspecial"
    # wordDict = ["go", "goal", "goals", "special"]

    # s = "aaaaaaa"
    # wordDict = ["aaaa", "aaa"]
    print(Solution().word_break(s, wordDict))
