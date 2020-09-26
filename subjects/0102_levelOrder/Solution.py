from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res, cur, tmp, upper, down = list(), root, list(), list(), list()
        while cur:
            tmp.append(cur.val)
            if cur.left:
                down.append(cur.left)
            if cur.right:
                down.append(cur.right)
            if not upper:
                res.append(tmp)
                tmp = list()
                upper = down
                down = list()
            cur = upper.pop(0) if upper else None

        return res
