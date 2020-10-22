# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur, n = head, 0
        while cur:
            n += 1
            cur = cur.next
        flag = ListNode(None)
        flag.next = head
        cur, pre_tail = head, flag
        for i in range(n // k):
            new_tail, pre = cur, None
            for j in range(k):
                tmp = cur.next
                if pre:
                    cur.next = pre
                pre = cur
                cur = tmp
            pre_tail.next = pre
            new_tail.next = cur
            pre_tail = new_tail
        return flag.next
