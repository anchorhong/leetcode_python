class Solution:
    def can_complete_circuit(self, gas, cost):
        n = len(gas)
        start = 0
        total, cur = 0, 0
        for i in range(n):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
        return start if total >= 0 else -1


if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(Solution().can_complete_circuit(gas, cost))
