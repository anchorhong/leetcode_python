from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        sum, finish = 0, -1
        for series in timeSeries:
            if finish >= series:
                sum -= finish - series + 1
            sum += duration
            finish = series + duration - 1
        return sum


if __name__ == "__main__":
    t = [1, 2]
    d = 2
    print(Solution().findPoisonedDuration(t, d))
