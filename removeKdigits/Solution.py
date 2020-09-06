class Solution:
    def removeKdigits(self, num: str, k):
        stack = []
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        res = stack[:-k] if k else stack
        return "".join(res).lstrip("0") or "0"


if __name__ == "__main__":
    num = "10"
    k = 0
    print(Solution().removeKdigits(num, k))
