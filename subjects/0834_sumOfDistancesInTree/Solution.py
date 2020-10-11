from typing import List


class Solution:
    def sum_of_distances_in_tree(self, N: int, edges: List[List[int]]) -> List[
        int]:
        edges.sort(key=lambda x: x[0])

