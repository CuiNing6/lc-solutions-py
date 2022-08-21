class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# class Solution:
#     def reverseKGroup(self , head , k ):
#         # write code here
#         if head ==None or head.next == None:
#             return head
#
#         dummy = ListNode(0)
#         dummy.next = head
#
#         start = dummy
#         end = dummy
#
#         while end.next != None:
#             for i in range(k):
#                 if end.next == None:
#                     break
#                 end = end.next
#
#             pre = start.next
#             next = end.next
#             end.next = None
#
#             start.next = self.ReverseList(pre)
#             pre.next = next
#
#             start = pre
#             end = pre
#
#         return dummy.next
#
#     def ReverseList(self, pHead):
#
#         pre = None
#         pnext = None
#
#         while pHead != None:
#             pnext = pHead.next
#             pHead.next = pre
#
#             pre = pHead
#             pHead = pnext
#
#         return pre


class Solution:
    def reverseKGroup(self , head , k ):
        # write code here
        if head ==None or head.next == None:
            return head

        tail = head

        for i in range(k):
            if tail==None:
                return head
            tail = tail.next

        res = self.ReverseList(head, tail)

        head.next = self.reverseKGroup(tail,k)

        return res



    def ReverseList(self, head, tail):

        pre = None
        pnext = None

        while head != tail:
            pnext = head.next
            head.next = pre

            pre = head
            head = pnext

        return pre


l1 = ListNode(1)
l1.next = ListNode(2)
# l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(4)
# l1.next.next.next.next = ListNode(5)
# l1.next.next.next.next.next = ListNode(6)
# l1.next.next.next.next.next.next = ListNode(7)

run = Solution()
l =  run.reverseKGroup(l1,2)
print (l.val, l.next.val)
# print (l.val, l.next.val, l.next.next.val, l.next.next.next.val, l.next.next.next.next.val, l.next.next.next.next.next.val,l.next.next.next.next.next.next.val)




