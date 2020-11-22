# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        guard = ListNode(float('-inf'))
        guard.next = head
        slow, cur, prev = guard, guard.next, guard
        while cur:
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
            else:
                if cur.val < head.val:
                    prev.next = cur.next
                    cur.next = head
                    guard.next = cur
                    head = cur
                else:
                    tmp = slow if cur.val >= slow.val else head
                    while tmp.next and tmp.next.val <= cur.val:
                        tmp = tmp.next
                    prev.next = cur.next
                    cur.next = tmp.next
                    tmp.next = cur
                    slow = cur
                cur = prev.next
        return guard.next


if __name__ == "__main__":
    [4, 19, 14, 5, -3, 1, 8, 5]
    n1 = ListNode(4)
    n2 = ListNode(19)
    n3 = ListNode(14)
    n4 = ListNode(5)
    n5 = ListNode(-3)
    n6 = ListNode(1)
    n7 = ListNode(8)
    n8 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    h = Solution().sortList(n1)
    print(h)
