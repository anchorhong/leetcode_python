# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def pre_successor(node: TreeNode):
            cur = node.left
            while cur.right:
                cur = cur.right
            return cur

        def successor(node: TreeNode):
            cur = node.right
            while cur.left:
                cur = cur.left
            return cur

        def traversal(tree: TreeNode):
            if not tree:
                return True
            if tree.left:
                if tree.left.val >= tree.val or pre_successor(tree) >= tree.val:
                    return False
                if traversal(tree.left) is False:
                    return False
            if tree.right:
                if tree.right.val <= tree.val or successor(tree) <= tree.val:
                    return False
                if traversal(tree.right) is False:
                    return False
            return True

        return traversal(root)

    def isValidBST(self, root: TreeNode) -> bool:
        def traversal(tree: TreeNode, lower=float('-inf'), upper=float('inf')) -> bool:
            if not tree:
                return True
            if tree.val <= lower or tree.val >= upper:
                return False
            return traversal(tree.left, lower, tree.val) and traversal(tree.right, tree.val, upper)

        return traversal(root)
