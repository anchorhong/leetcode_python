class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        root.next = None

        def traversal(tree: Node, parent: Node, is_left: bool):
            if not tree:
                return
            if is_left and parent.right:
                tree.next = parent.right
            elif parent.next:
                cur = parent.next
                while cur:
                    if cur.left:
                        tree.next = cur.left
                        break
                    elif cur.right:
                        tree.next = cur.right
                        break
                    else:
                        cur = cur.next
            traversal(tree.right, tree, False)
            traversal(tree.left, tree, True)

        traversal(root.right, root, False)
        traversal(root.left, root, True)
        return root
