class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
class Solution:
    def deleteDuplicates(self , head ):
        # write code here
        if head == None or head.next == None:
            return head

        res = ListNode(0)
        res.next = head

        p = res
        q = head

        while q!=None and q.next!=None:
            if q.next.val != q.val:
                p = q
                q = q.next
            else:
                while q.next!=None and q.next.val == q.val:
                    q = q.next
                q = q.next
                p.next = q

        return  res.next


l1 = ListNode(1)
l1.next = ListNode(5)
l1.next.next = ListNode(5)
l1.next.next.next = ListNode(7)

l2 = ListNode(1)
l2.next = ListNode(1)

run = Solution()
l =  run.deleteDuplicates(l1)
print (l.val, l.next.val)