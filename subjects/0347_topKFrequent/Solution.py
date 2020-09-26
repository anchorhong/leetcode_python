from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_dict = defaultdict(int)
        for num in nums:
            top_dict[num] += 1
        values = list(top_dict.keys())
        values.sort(key=lambda x: top_dict.get(x), reverse=True)
        res = list()
        for i in range(k):
            res.append(values[i])

        return res

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent2(nums, k))
    nums = [1]
    k = 1
    print(Solution().topKFrequent2(nums, k))
