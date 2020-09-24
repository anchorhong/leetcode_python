# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        root = TreeNode(postorder.pop())
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                left_in = inorder[:i]
                right_in = inorder[i + 1:]
                left_post = postorder[:len(left_in)]
                right_post = postorder[-len(right_in):] if len(
                    right_in) != 0 else list()
                root.left = self.buildTree(left_in, left_post)
                root.right = self.buildTree(right_in, right_post)

        return root


if __name__ == "__main__":
    ino = [2, 1]
    post = [2, 1]
    print(Solution().buildTree(ino, post))
