# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(child: TreeNode, parent: TreeNode) -> int:
            if child.left:
                if not child.left.left:
                    child.left.val = 1
                dfs(child.left, child)