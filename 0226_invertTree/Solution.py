class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root_left, root_right = root.left, root.right
            new_left = self.invertTree(root_left)
            root.right = new_left
            new_left = self.invertTree(root_right)
            root.left = new_left
        return root
