class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = list()
        for i in range(len(num)):
            if k == 0:
                stack.extend(num[i:])
                break
            while k and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        res = stack[:-k] if k else stack
        return "".join(res).lstrip("0") or "0"


if __name__ == "__main__":
    num = "1432219"
    k = 3
    # num = "10200"
    # k = 1
    # num = "1234567890"
    # k = 9
    print(Solution().removeKdigits(num, k))
