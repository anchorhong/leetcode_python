# https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res, stack, layer_sum, num = list(), [root, None], 0, 0
        while stack:
            cur = stack.pop(0)
            if cur:
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
                layer_sum += cur.val
                num += 1
            else:
                res.append(layer_sum / num)
                layer_sum, num = 0, 0
                if stack:
                    stack.append(None)
        return res
