class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        times = 0
        if dividend < 0 and divisor < 0:
            while dividend <= divisor:
                dividend -= divisor
                times += 1
        elif dividend < 0 < divisor:
            while dividend <= 0 - divisor:
                dividend += divisor
                times -= 1
        elif divisor > 0 and dividend > 0:
            while dividend >= divisor:
                dividend -= divisor
                times += 1
        elif divisor < 0 < dividend:
            while dividend >= 0 - divisor:
                dividend += divisor
                times -= 1
        return times
