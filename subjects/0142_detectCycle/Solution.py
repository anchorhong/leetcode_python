class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detect_cycle(self, head: ListNode) -> ListNode:
        s, cur = set(), head
        while cur:
            if cur in s:
                return cur
            s.add(cur)
            cur = cur.next
        return None

    def detect_cycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        fast, slow = head, head
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return None
            if fast == slow:
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None
