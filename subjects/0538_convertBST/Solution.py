class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def greater_sum(parent: TreeNode):
            nonlocal tree_sum
            if parent:
                greater_sum(parent.right)
                tree_sum += parent.val
                parent.val = tree_sum
                greater_sum(parent.left)
        total = 0
        greater_sum(root)
        return root
