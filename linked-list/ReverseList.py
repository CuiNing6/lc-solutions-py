# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead

        pre = None
        pnext = None

        while pHead != None:
            pnext = pHead.next
            pHead.next = pre

            pre = pHead
            pHead = pnext

        return pre

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

run = Solution()
l =  run.ReverseList(l1)
print (l.val, l.next.val, l.next.next.val)