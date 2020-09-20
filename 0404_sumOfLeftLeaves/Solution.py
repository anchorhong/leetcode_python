class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        cur, pre, res = root.left, None, 0
        while cur:
            pre = cur
            if cur.right:
                res += self.sumOfLeftLeaves(cur.right)
            cur = cur.left
        if pre and pre.right is None:
            res += pre.val
        if root.right:
            res += self.sumOfLeftLeaves(root.right)
        return res

    def sum_of_left_leaves_1(self, root: TreeNode) -> int:
        is_leaf_node = lambda node: not node.left and not node.right

        def dfs(node: TreeNode) -> int:
            res = 0
            if node.left:
                res += node.left.val if is_leaf_node(node.left) else dfs(
                    node.left)
            if node.right and not is_leaf_node(node.right):
                res += dfs(node.right)
            return res

        return dfs(root) if root else 0
