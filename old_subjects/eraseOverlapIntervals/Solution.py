class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x: (x[1], x[0]))
        origin_len = len(intervals)
        end_value = intervals.pop(0)[1]
        cur_len = 1
        for i in intervals:
            if i[0] >= end_value:
                cur_len += 1
                end_value = i[1]
        return origin_len - cur_len


if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(Solution().eraseOverlapIntervals(intervals))
