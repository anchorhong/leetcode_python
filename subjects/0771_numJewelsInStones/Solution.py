class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j_set = set()
        for j in J:
            j_set.add(j)
        num = 0
        for s in S:
            if s in j_set:
                num += 1
        return num
