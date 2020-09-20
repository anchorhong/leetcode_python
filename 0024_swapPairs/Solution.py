class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ppre, pre, cur, times = None, None, head, 0
        while cur:
            times += 1
            if times == 2:
                if ppre:
                    ppre.next, pre.next, cur.next = cur, cur.next, pre
                    pre, cur = cur, cur.next
                else:
                    x, pre.next = pre, cur.next
                    cur.next = x
                    pre = cur
                    head = pre
                    cur = x
                times = 0
            ppre, pre, cur = pre, cur, cur.next
        return head
