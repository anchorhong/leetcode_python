class Solution:
    def updateMatrix(self, matrix):
        res = [[float('inf') for _ in range(len(matrix[0]))] for _ in
               range(len(matrix))]
        for i in range(len(res)):
            for j in range(len(res[0])):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i > 0:
                        res[i][j] = min(res[i][j], res[i - 1][j] + 1)
                    if j > 0:
                        res[i][j] = min(res[i][j], res[i][j - 1] + 1)

        for i in range(len(res) - 1, -1, -1):
            for j in range(len(res[0]) - 1, -1, -1):
                if i < len(res) - 1:
                    res[i][j] = min(res[i][j], res[i + 1][j] + 1)
                if j < len(res[0]) - 1:
                    res[i][j] = min(res[i][j], res[i][j + 1] + 1)

        return res


if __name__ == '__main__':
    q = [[0], [1]]
    print(Solution().updateMatrix(q))
