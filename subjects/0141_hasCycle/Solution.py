class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def has_cycle(self, head: ListNode) -> bool:
        pos, cur, i = -1, head, -1
        s = set()
        while cur:
            i += 1
            if cur in s:
                pos = i
                break
            s.add(cur)
            cur = cur.next
        return pos != -1

    def has_cycle(self, head: ListNode) -> bool:
        cur = head
        while cur:
            if not cur.val:
                return True
            cur.val = None
            cur = cur.next
        return False

    def has_cycle(self, head: ListNode) -> bool:
        if not head:
            return True
        slow, fast, i = head, head.next, 1
        while fast:
            if fast == slow:
                return True
            fast = fast.next
            i += 1
            slow = slow.next if i % 2 == 0 else slow
        return False
