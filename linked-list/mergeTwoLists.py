class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self , l1 , l2 ):
        # write code here
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        res = ListNode(0)
        tmp = res

        while l1!=None and l2!=None:
            if l1.val >= l2.val:
                tmp.next = l2
                l2 = l2.next
            else:
                tmp.next = l1
                l1  = l1.next
            tmp = tmp.next

        if l1 is not None:
            tmp.next = l1
        else:
            tmp.next = l2

        return res.next

l1 = ListNode(1)
l1.next = ListNode(5)
l1.next.next = ListNode(7)

l2 = ListNode(2)
l2.next = ListNode(6)
l2.next.next = ListNode(8)

run = Solution()
l =  run.mergeTwoLists(l1,l2)
print (l.val, l.next.val, l.next.next.val,l.next.next.next.val,l.next.next.next.next.val,l.next.next.next.next.next.val)