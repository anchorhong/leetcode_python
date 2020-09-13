# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#  
#
# 示例:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#  
#
# 提示：
#
# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-search
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
from typing import Set
from typing import Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        coord, res = set(), list()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(i: int, j: int, n: int) -> bool:
            if board[i][j] != word[n]:
                return False
            if n == len(word) - 1:
                return True
            coord.add((i, j))
            for di, dj in directions:
                n_i, n_j = i + di, j + dj
                if 0 <= n_i < len(board) and 0 <= n_j < len(board[0]) and (
                        n_i, n_j) not in coord:
                    if dfs(n_i, n_j, n + 1):
                        return True
            coord.remove((i, j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False


if __name__ == "__main__":
    board = [
        ["C", "A", "A"],
        ["A", "A", "A"],
        ["B", "C", "D"]]
    word = "AAB"
    print(Solution().exist(board, word))
