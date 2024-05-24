# -*- coding:UTF-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
两个链表生成相加链表
描述
假设链表中每一个节点的值都在 0 - 9 之间，那么链表整体就可以代表一个整数。
给定两个这种链表，请生成代表两个整数相加值的结果链表。
例如：链表 1 为 9->3->7，链表 2 为 6->3，最后生成新的结果链表为 1->0->0->0。

输入：[9,3,7],[6,3]
返回值：{1,0,0,0}
'''

class Solution:
    def addInList(self , head1 , head2 ):
        # write code here
        head1_num = []
        head2_num = []

        while head1:
            head1_num.append(head1.val)
            head1 = head1.next

        while head2:
            head2_num.append(head2.val)
            head2 = head2.next

        num1 = int(''.join(str(x) for x in head1_num))
        num2 = int(''.join(str(x) for x in head2_num))

        num = num1 + num2

        num_list = [int(x) for x in ','.join(str(num)).split(',')]

        res = ListNode(0)
        head = res
        for j in num_list:
            head.next = ListNode(j)
            head = head.next

        return res.next

    def addInList2(self , head1 , head2 ):
        # write code here
        pre1 = None
        pre2 = None

        while head1:
            temp1 = head1.next
            head1.next = pre1
            pre1 = head1
            head1 = temp1


        while head2:
            temp2 = head2.next
            head2.next = pre2
            pre2 = head2
            head2 = temp2

        flag = 0
        res = ListNode(0)
        head = res

        while pre1 and pre2:
            head.next = ListNode(int((pre1.val + pre2.val + flag) % 10))
            flag = (pre1.val + pre2.val + flag) / 10
            head = head.next
            pre1 = pre1.next
            pre2 = pre2.next

        while pre1:
            head.next = ListNode(int((pre1.val + flag) % 10))
            flag = (pre1.val + flag) / 10
            head = head.next
            pre1 = pre1.next

        while pre2:
            head.next = ListNode(int((pre2.val + flag) % 10))
            flag = (pre2.val + flag) / 10
            head = head.next
            pre2 = pre2.next

        if flag != 0:
            head.next = ListNode(int(flag))

        head3 = res.next
        pre3 = None
        while head3:
            temp3 = head3.next
            head3.next = pre3
            pre3 = head3
            head3 = temp3

        return pre3


l1 = ListNode(9)
l1.next = ListNode(3)
l1.next.next = ListNode(7)

l2 = ListNode(6)
l2.next = ListNode(3)

run = Solution()
r = run.addInList2(l1, l2)
print (r.val,r.next.val,r.next.next.val,r.next.next.next.val)