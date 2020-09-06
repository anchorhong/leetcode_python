import collections


class Solution():
    def isPossible(self, nums):
        count = collections.Counter(nums)
        chain = collections.Counter()
        for x in nums:
            if count[x] == 0:
                continue
            elif chain[x] > 0:
                chain[x] -= 1
                chain[x + 1] += 1
            elif count[x + 1] > 0 and count[x + 2] > 0:
                count[x + 1] -= 1
                count[x + 2] -= 1
                chain[x + 3] += 1
            else:
                return False
            count[x] -= 1
        return True
