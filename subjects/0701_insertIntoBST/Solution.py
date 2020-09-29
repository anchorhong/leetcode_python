class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        new_node = TreeNode(val)
        if not root:
            return new_node
        cur, prev = root, None
        while cur:
            if val < cur.val:
                prev = cur
                cur = cur.left
            elif val > cur.val:
                prev = cur
                cur = cur.right
        if val < prev.val:
            prev.left = new_node
        else:
            prev.right = new_node
        return root
