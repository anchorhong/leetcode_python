from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> \
            List[List[int]]:
        res = list()
        left, right = newInterval[0], newInterval[1]
        need_insert = True
        for interval in intervals:
            if need_insert:
                if interval[0] > right:
                    res.append([left, right])
                    need_insert = False
                    res.append(interval)
                elif interval[1] < left:
                    res.append(interval)
                else:
                    left = min(interval[0], left)
                    right = max(interval[1], right)
            else:
                res.append(interval)
        if need_insert:
            res.append([left, right])
        return res


if __name__ == "__main__":
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 10]
    print(Solution().insert(intervals, newInterval))
    # intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    # newInterval = [4, 8]
    # print(Solution().insert(intervals, newInterval))
