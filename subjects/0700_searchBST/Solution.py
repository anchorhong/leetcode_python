# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        cur = root
        while cur:
            if val == cur.val:
                return cur
            elif val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return None