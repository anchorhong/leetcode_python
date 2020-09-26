from typing import List


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res, upper, down, tmp, cur = list(), list(), list(), list(), root
        while cur:
            tmp.append(cur.val)
            if cur.left:
                down.append(cur.left)
            if cur.right:
                down.append(cur.right)
            if len(upper) == 0:
                res.insert(0, tmp)
                tmp = []
                upper = down
                down = []
            cur = upper.pop(0) if upper else None

        return res
