#coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类 the head node
# @return ListNode类
#
class Solution:
    def sortInList(self , head ):
        # write code here
        if not head:
            return None

        res = []

        while head:
            res.append(head.val)
            head = head.next

        res.sort()

        reshead = ListNode(0)
        phead = reshead

        for i in res:
            phead.next = ListNode(i)
            phead = phead.next

        return reshead.next

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(2)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

run = Solution()
l =  run.sortInList(l1)
print (l.val,l.next.val,l.next.next.val,l.next.next.next.val,l.next.next.next.next.val)