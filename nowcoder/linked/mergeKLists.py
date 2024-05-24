#coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param lists ListNode类一维数组
# @return ListNode类
#
class Solution:
    def mergeKLists(self , lists ):
        # write code here
        if len(lists) == 0:
            return []
        if len(lists) == 1:
            return lists[0]

        res = []
        for i in lists:
            while i:
                res.append(i.val)
                i = i.next

        res.sort()
        head1 = phead = ListNode(0)

        for j in res:
            phead.next = ListNode(0)
            phead = phead.next
            phead.val = j

        return head1.next

    def merge2Lists(self , lists ):
        # write code here
        l1 = lists[0]
        l2 = lists[1]

        head1 = phead = ListNode(0)

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                phead.next = l1
                l1 = l1.next
            else:
                phead.next = l2
                l2 = l2.next

            phead = phead.next

        if l1 != None:
            phead.next = l1
        else:
            phead.next = l2

        return head1.next


lists = []
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
lists.append(l1)

l2 = ListNode(4)
l2.next = ListNode(5)
l2.next.next = ListNode(6)
lists.append(l2)

l3 = ListNode(7)
l3.next = ListNode(8)
l3.next.next = ListNode(9)
# lists.append(l3)


run = Solution()
#l =  run.mergeKLists(lists)
#print (l.val, l.next.val, l.next.next.val,l.next.next.next.val,l.next.next.next.next.val,l.next.next.next.next.next.val,l.next.next.next.next.next.next.val,l.next.next.next.next.next.next.next.val,l.next.next.next.next.next.next.next.next.val)

l =  run.merge2Lists(lists)
print (l.val, l.next.val, l.next.next.val,l.next.next.next.val,l.next.next.next.next.val,l.next.next.next.next.next.val)



