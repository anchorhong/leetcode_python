# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        max_times, max_value = 1, list()
        max_value.append(root.val)

        def dfs(tree: TreeNode, parent: TreeNode, result: List[int]) -> int:
            nonlocal max_times
            if not tree:
                return 0
            else:
                times = 1
                times += dfs(tree.left, tree, result)
                times += dfs(tree.right, tree, result)
                if times == max_times and tree.val not in max_value:
                    result.append(tree.val)
                if times > max_times:
                    result.clear()
                    result.append(tree.val)
                    max_times = times
                if tree.val == parent.val:
                    return times
                else:
                    return 0

        dfs(root.left, root, max_value)
        dfs(root.right, root, max_value)
        return max_value


if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)
    t1.right = t2
    t2.left = t3
    print(Solution().findMode(t1))
