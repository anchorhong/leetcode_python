class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        flag = ListNode(None)
        flag.next = head
        cur, n = flag, 0
        while cur.next:
            n += 1
            cur = cur.next
        span = n // 2 if n % 2 == 0 else n // 2 + 1
        cur, i, pre, slow = head, 0, None, None
        while cur.next:
            if i < (n // 2):
                tmp = cur.next
                cur.next, pre, cur = pre, cur, tmp
            else:
                if pre:
                    flag.next, head.next, pre = pre, cur, None
                else:
                    cur = cur.next
                    slow = slow.next if slow else None
                    if slow is not None and slow.val != cur.val:
                        return False
            i += 1
            slow = flag if i == span else slow
        return True


if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
    print(Solution().isPalindrome(l1))
