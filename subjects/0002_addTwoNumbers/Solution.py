from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None, None)
        cur, carry = head, 0
        while l1 or l2:
            op1 = l1.val if l1 else 0
            op2 = l2.val if l2 else 0
            s = (op1 + op2 + carry) % 10
            carry = (op1 + op2 + carry) // 10
            new_node = ListNode(s, None)
            cur.next = new_node
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry == 1:
            new_node = ListNode(carry, None)
            cur.next = new_node
        return head.next
