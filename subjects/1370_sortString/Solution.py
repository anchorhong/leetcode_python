from collections import OrderedDict
from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        bucket = Counter(s)
        res = list()
        is_increase = False
        while len(bucket.keys()) > 0:
            key_list = list(bucket.keys())
            key_list.sort(reverse=is_increase)
            is_increase = False if is_increase else True
            for k in key_list:
                bucket[k] -= 1
                if bucket[k] == 0:
                    del bucket[k]
            res.extend(key_list)
        return ''.join(res)


if __name__ == "__main__":
    s = "rat"
    print(Solution().sortString(s))
