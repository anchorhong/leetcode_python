# https://leetcode-cn.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res, total_len, = list(), len(s)
        fixed_span = int(2 * numRows - 2) if int(2 * numRows - 2) != 0 else 1
        for row in range(numRows):
            if row == 0 or row == numRows - 1:
                idx = row
                while idx < total_len:
                    res.append(s[idx])
                    idx += fixed_span

            else:
                span = int(2 * (numRows - row - 1))
                idx_1, idx_2 = row, row + span
                while idx_1 < total_len or idx_2 < total_len:
                    if idx_1 < total_len:
                        res.append(s[idx_1])
                        idx_1 += fixed_span
                    if idx_2 < total_len:
                        res.append((s[idx_2]))
                        idx_2 += fixed_span
        return ''.join(map(str, res))


if __name__ == "__main__":
    print(Solution().convert("LEETCODEISHIRING", 1))
