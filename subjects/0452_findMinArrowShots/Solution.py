from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))
        nums = 0
        minx, maxx = float('inf'), float('-inf')
        for point in points:
            if minx <= point[0] <= maxx:
                minx = max(minx, point[0])
                maxx = min(maxx, point[1])
            else:
                nums += 1
                minx, maxx = point[0], point[1]
        return nums


if __name__ == "__main__":
    points = [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
    print(Solution().findMinArrowShots(points))
