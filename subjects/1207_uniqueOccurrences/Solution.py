from typing import List
from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = defaultdict(int)
        for a in arr:
            counts[a] += 1
        return len(counts.keys()) == len(set(counts.values()))