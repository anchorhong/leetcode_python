# https://leetcode-cn.com/problems/find-common-characters/
from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def common_chars(A: List[str]) -> List[str]:
        char_dict = None
        for word in A:
            word_dict = defaultdict(int)
            for c in word:
                word_dict[c] += 1
            if char_dict is not None:
                and_dict = defaultdict(int)
                for key in word_dict.keys() & char_dict.keys():
                    and_dict[key] = min(char_dict[key], word_dict[key])
                char_dict = and_dict
            else:
                char_dict = word_dict
        res = list()
        for key, value in char_dict.items():
            for times in range(value):
                res.append(key)
        return res
