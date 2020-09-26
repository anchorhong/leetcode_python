# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        self.__traverse(root, res)
        return res

    def __traverse(self, parent: TreeNode, res: List[int]):
        if parent.left:
            self.__traverse(parent.left, res)
        res.append(parent.val)
        if parent.right:
            self.__traverse(parent.right, res)


class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack,parent = list(), [root],root
        while parent:
            if parent.left:
                stack.append(parent.left)
                parent = parent.left
            else:
                top = stack.pop()
                res.append(top.val)
                while top.right is None and stack:
                    top = stack.pop()
                    res.append(top.val)
                if top.right:
                    stack.append(top.right)
                    parent = top.right
                else:
                    parent = None
        return res
