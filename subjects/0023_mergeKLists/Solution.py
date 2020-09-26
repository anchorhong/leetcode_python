from typing import List
import heapq


# lists = [[1,4,5],[1,3,4],[2,6]]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        val_list = list()
        for lst in lists:
            cur = lst
            while cur:
                val_list.append(cur.val)
                cur = cur.next
        heapq.heapify(val_list)
        res = ListNode(None, None)
        cur = res
        while val_list:
            v = heapq.heappop(val_list)
            cur.next = ListNode(v, None)
            cur = cur.next
        return res.next
