# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def countNodes(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #
    #     def tree_level(node: TreeNode) -> int:
    #         level = 0
    #         while node:
    #             level += 1
    #             node = node.left
    #         return level
    #
    #     left_level, right_level = tree_level(root.left), tree_level(root.right)
    #
    #     if left_level == right_level:
    #         return self.countNodes(root.right) + (1 << left_level)
    #     else:
    #         return self.countNodes(root.left) + (1 << right_level)
    #
    # def countNodes(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def exists(tree: TreeNode, level: int, k: int) -> bool:
            bits = 1 << (level - 1)
            cur = tree
            while cur and bits > 0:
                if bits & k == 0:
                    cur = cur.left
                else:
                    cur = cur.right
                bits >>= 1
            return cur is not None

        level = 0
        cur = root
        while cur.left:
            level += 1
            cur = cur.left
        low, high = 1 << level, (1 << (level + 1)) - 1
        while low < high:
            mid = (high - low + 1) // 2 + low
            if exists(root, level, mid):
                low = mid
            else:
                high = mid - 1
        return low


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    print(Solution().countNodes(n1))
