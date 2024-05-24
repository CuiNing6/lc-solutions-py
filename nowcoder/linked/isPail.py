#coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类 the head
# @return bool布尔型
# 判断一个链表是否为回文结构
class Solution:
    def isPail(self , head ):
        # write code here
        if not head:
            return False

        if not head.next:
            return True

        phead, slow, fast = head, head, head

        while fast and fast.next:
            phead = slow
            slow = slow.next
            fast = fast.next.next
        phead.next = None

        pre = self.reverse(slow)

        while head and pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next

        return True

    def reverse(self,head):
        cur = head
        head = None
        while cur:
            tmp = cur.next
            cur.next = head
            head = cur
            cur = tmp

        return head

#1,2,3,4,5,4,3,2,1,1
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(4)
l1.next.next.next.next.next.next = ListNode(3)
l1.next.next.next.next.next.next.next = ListNode(2)
l1.next.next.next.next.next.next.next.next = ListNode(1)
l1.next.next.next.next.next.next.next.next.next = ListNode(1)

run = Solution()
l =  run.isPail(l1)
print (l)