class Solution:
    def predictPartyVictory(self, senate):
        senates = [s for s in senate]
        part_r, part_d, i = 0, 0, 0
        while i < len(senates) and part_d != len(senates) and part_r != len(senates):
            if senates[i] == "R" and part_d == 0:
                part_r += 1
                i = i + 1 if i < len(senates) - 1 else 0
            elif senates[i] == "D" and part_r == 0:
                part_d += 1
                i = i + 1 if i < len(senates) - 1 else 0
            elif senates[i] == "R" and part_d > 0:
                senates.pop(i)
                part_d -= 1
                i = i if i < len(senates) else 0
            elif senates[i] == "D" and part_r > 0:
                senates.pop(i)
                part_r -= 1
                i = i if i < len(senates) else 0
        return "Dire" if part_d != 0 else "Radiant"


if __name__ == "__main__":
    n = "DR"
    print(Solution().predictPartyVictory(n))
