# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    @staticmethod
    def connect(root: 'Node') -> 'Node':
        def traverse(tree: Node, parent: Node):
            if not tree:
                return
            if parent and parent.right == tree and parent.next:
                tree.next = parent.next.left
            elif parent and parent.left == tree:
                tree.next = parent.right
            traverse(tree.right, tree)
            traverse(tree.left, tree)

        traverse(root, None)
        return root
