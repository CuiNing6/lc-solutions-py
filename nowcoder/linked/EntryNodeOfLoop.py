# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None

        fast = pHead
        slow = pHead

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast.val == slow.val:
                while slow.val != pHead.val:
                    slow = slow.next
                    pHead = pHead.next

                return slow

        return None


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)
l1.next.next.next.next.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)

run = Solution()
l =  run.EntryNodeOfLoop(l1)
print (l.val)

