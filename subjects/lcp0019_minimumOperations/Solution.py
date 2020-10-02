class Solution:
    def minimumOperations(self, leaves: str) -> int:
        f = [[0, 0] for _ in range(len(leaves))]
        f[0][0] = int(leaves[0] == "y")
        f[0][1] = f[1][0] = f[1][2] = float("inf")
        for i in range(1, len(leaves)):
            is_yellow = int(leaves[i] == "y")
            is_red = int(leaves[i] == "r")
            f[i][0] = f[i - 1][0] + is_yellow
            f[i][1] = min(f[i - 1][0], f[i - 1][1]) + is_red
            if i > 1:
                f[i][2] = min(f[i - 1][1], f[i - 1][2]) + is_yellow
        return f[len(leaves) - 1][2]
