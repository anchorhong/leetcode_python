from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = list()

        def dfs(parent: TreeNode, total: int, combine: List[int]):
            nonlocal res, sum
            if not parent:
                return
            combine.append(parent.val)
            total += parent.val
            if not parent.left and not parent.right and total == sum:
                res.append(combine)
                return
            dfs(parent.left, total, combine.copy())
            dfs(parent.right, total, combine.copy())

        dfs(root, 0, list())
        return res
