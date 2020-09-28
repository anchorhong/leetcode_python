from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recursive_traversal(root: TreeNode) -> List[int]:
    if not root:
        return []

    def traversal(parent: TreeNode, res: List[int]):
        if not parent:
            return
        traversal(parent.left, res)
        res.append(parent.val)
        traversal(parent.right, res)

    result = list()
    traversal(root, result)
    return result


def iterate_traversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    stack, res = [root], list()
    cur = root.left
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right


# def morris_traversal(root: TreeNode) -> List[int]:

