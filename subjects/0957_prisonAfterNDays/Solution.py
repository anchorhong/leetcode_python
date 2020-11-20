from typing import List
from collections import defaultdict


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def nextDay(today):
            return [int(i > 0 and i < len(today) - 1 and today[i - 1] == today[i + 1]) for i in
                    range(len(today))]

        cached = defaultdict(int)
        i = 1
        today = cells
        while 0 < N:
            next_day = nextDay(today)
            if next_day not in cached.values():
                cached[i] = next_day
            else:
                break
            i += 1
            today = next_day
        num = len(cached.keys())
        N = N % num
        return cached[N]


if __name__ == "__main__":
    cells = [1,1,0,0,0,0,1,1]
    N = 7
    print(Solution().prisonAfterNDays(cells, N))
