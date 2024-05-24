#coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def oddEvenList(self , head ):
        # write code here
        if not head:
            return None

        phead_odd = ListNode(0)
        odd = phead_odd
        phead_even = ListNode(0)
        even = phead_even

        flag = 1
        while head != None:
            if flag % 2 == 0:
                odd.next = ListNode(head.val)
                odd = odd.next
            else:
                even.next = ListNode(head.val)
                even = even.next
            flag += 1
            head = head.next

        even.next = phead_odd.next

        return phead_even.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)

run = Solution()
l =  run.oddEvenList(l1)
print (l.val,l.next.val,l.next.next.val,l.next.next.next.val,l.next.next.next.next.val,l.next.next.next.next.next.val)