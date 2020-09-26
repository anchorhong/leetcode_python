from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor_0(self, root: TreeNode, p: TreeNode,
                               q: TreeNode) -> TreeNode:
        path_p, path_q = None, None

        def traversal(cur: TreeNode, path: List[TreeNode]):
            nonlocal path_p, path_q
            if not cur:
                return
            path.append(cur)
            if cur.val == p.val:
                path_p = path.copy()
            elif cur.val == q.val:
                path_q = path.copy()
            traversal(cur.left, path.copy())
            traversal(cur.right, path.copy())

        traversal(root, list())
        max_height = min(len(path_p), len(path_q))
        for i in range(max_height - 1, -1, -1):
            if path_p[i] == path_q[i]:
                return path_p[i]

    def lowestCommonAncestor_1(self, root: TreeNode, p: TreeNode,
                               q: TreeNode) -> TreeNode:
        cur = root
        while cur:
            if p.val < cur.val < q.val or q.val < cur.val < p.val:
                return cur
            elif p.val == cur.val:
                return p
            elif q.val == cur.val:
                return q
            elif q.val < cur.val and p.val < cur.val:
                cur = cur.left
            else:
                cur = cur.right


if __name__ == "__main__":
    t1 = TreeNode(6)
    t2 = TreeNode(2)
    t3 = TreeNode(8)
    t1.left = t2
    t1.right = t3
    print(Solution().lowestCommonAncestor_1(t1, t2, t3).val)
