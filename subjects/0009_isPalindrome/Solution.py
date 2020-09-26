# https://leetcode-cn.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        base = 10
        while int(x / base) != 0:
            base *= 10
        while x != 0:
            hi = int(x * 10 / base)
            lo = x % 10
            if hi != lo:
                return False
            x = int(x % (base / 10) / 10)
            base = int(base / 100)

        return True


if __name__ == "__main__":
    print(Solution().isPalindrome(10111))
