class Solution:
    def reconstructQueue(self, people: list[list[int]]):
        people.sort(lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
