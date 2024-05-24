#coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head1 ListNode类
# @param head2 ListNode类
# @return ListNode类
#
class Solution:
    def addInList(self , head1 , head2 ):
        # write code here
        if not head1 and not head2:
            return 0
        if not head1:
            return head2
        if not head2:
            return head1

        cur1 = head1
        pre1 = None
        while cur1:
            tmp1 = cur1.next
            cur1.next = pre1
            pre1 = cur1
            cur1 = tmp1

        cur2 = head2
        pre2 = None
        while cur2:
            tmp2 = cur2.next
            cur2.next = pre2
            pre2 = cur2
            cur2 = tmp2


        phead = ListNode(0)
        res = phead
        flag = 0
        while pre1 or pre2:
            if not pre1:
                nums = pre2.val + flag
                flag = nums / 10
                res.next = ListNode(int(nums % 10))
                pre2 = pre2.next
                res = res.next
            elif not pre2:
                nums = pre1.val + flag
                flag = nums / 10
                res.next = ListNode(int(nums % 10))
                pre1 = pre1.next
                res = res.next
            else:
                nums = pre1.val + pre2.val + flag
                flag = nums / 10
                res.next = ListNode(int(nums % 10))
                pre1 = pre1.next
                pre2 = pre2.next
                res = res.next

        if flag > 0:
            res.next = ListNode(int(flag))


        cur3 = phead.next
        pre3 = None
        while cur3:
            tmp3 = cur3.next
            cur3.next = pre3
            pre3 = cur3
            cur3 = tmp3

        return pre3

l1 = ListNode(9)
l1.next = ListNode(3)
l1.next.next = ListNode(7)

l2 = ListNode(6)
l2.next = ListNode(3)


run = Solution()
l =  run.addInList(l1, l2)
print (l.val, l.next.val, l.next.next.val,l.next.next.next.val)



def reverse(l1):
    if not l1:
        return None

    cur = l1
    pre = None

    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp

    return pre

# l2 = ListNode(6)
# l2.next = ListNode(3)

# l = reverse(l2)
# print (l.val, l.next.val)