from typing import List
import heapq
from collections import defaultdict


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K == 0:
            return []
        point_dict = defaultdict(list)
        max_heap = list()
        for point in points:
            distance = 0 - (point[0] ** 2 + point[1] ** 2)
            if len(max_heap) < K:
                heapq.heappush(max_heap, distance)
                point_dict[distance].append(point)
            if len(max_heap) >= K and distance > max_heap[0]:
                max_distance = heapq.heappop(max_heap)
                point_dict[max_distance].pop()
                if not point_dict[max_distance]:
                    del point_dict[max_distance]
                heapq.heappush(max_heap, distance)
                point_dict[distance].append(point)

        res = list()
        for v in point_dict.values():
            res.extend(v)
        return res


if __name__ == "__main__":
    # points = [[-95, 76], [17, 7], [-55, -58], [53, 20], [-69, -8], [-57, 87], [-2, -42], [-10, -87],
    points = [[1,3],[-2,2]]

    K = 1
    print(Solution().kClosest(points, K))
