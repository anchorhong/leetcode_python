from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = [0] * 26
        for i in range(len(S)):
            last[ord(S[i]) - ord('a')] = i
        start, end, res = 0, 0, list()
        for i in range(len(S)):
            end = max(end, last[ord(S[i]) - ord('a')])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res

