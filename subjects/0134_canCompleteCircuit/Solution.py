from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i, n = 0, len(gas)
        while i < n:
            reserved = gas[i] - cost[i]
            if reserved < 0:
                i += 1
            else:
                j = i + 1 if i < n - 1 else 0
                while j != i and reserved >= 0:
                    reserved += gas[i] - cost[i]
                    j = j + 1 if j < n - 1 else 0
                if reserved < 0:
                    i = j + 1
                if j == i:
                    return i
        return -1


if __name__ == "__main__":
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    print(Solution().canCompleteCircuit(gas, cost))
