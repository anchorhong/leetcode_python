# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(tree_1: TreeNode, tree_2: TreeNode, parent, is_left: bool):
            if tree_1 and tree_2:
                tree_1.val = tree_1.val + tree_2.val
                dfs(tree_1.left, tree_2.left, tree_1, True)
                dfs(tree_1.right, tree_2.right, tree_1, False)
            if not tree_1 and tree_2:
                if is_left:
                    parent.left = tree_2
                else:
                    parent.right = tree_2

        flag = TreeNode()
        flag.left = t1
        dfs(t1, t2, flag, True)
        return flag.left

    def mergeTrees_1(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        merged = TreeNode(t1.val + t2.val, None, None)
        merged.left = self.mergeTrees_1(t1.left, t2.left)
        merged.right = self.mergeTrees_1(t1.right, t2.right)

        return merged
