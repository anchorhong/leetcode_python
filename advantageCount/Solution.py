class Solution:
    def advantageCount(self, A, B):
        sortA = sorted(A)
        sortB = sorted(B)

        b_res = {b: [] for b in B}
        remain = []
        j = 0
        for a in sortA:
            if a > sortB[j]:
                b_res[sortB[j]].append(a)
                j += 1
            else:
                remain.append(a)

        return [b_res[b].pop() if b_res[b] else remain.pop() for b in B]


if __name__ == '__main__':
    A = [2, 0, 4, 1, 2]
    B = [1, 3, 0, 0, 2]
    print(Solution().advantageCount(A, B))
