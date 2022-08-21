class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        if pHead1 == None or pHead2 == None:
            return None

        p1 = pHead1
        p2 = pHead2

        while p1.val!=p2.val:
            # print (p1.val)
            # print (p2.val)
            # print ("#######")
            p1 = p1.next
            p2 = p2.next

            if p1!=p2:
                if p1 == None:
                    p1 = pHead2
                elif p2 == None:
                    p2 = pHead1

        return p1

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(5)
l1.next.next.next.next = ListNode(6)

l2 = ListNode(2)
l2.next = ListNode(7)
l2.next.next = ListNode(8)
l2.next.next.next = ListNode(9)
l2.next.next.next.next = ListNode(5)
l2.next.next.next.next.next = ListNode(6)


run = Solution()
l =  run.FindFirstCommonNode(l1, l2)
print (l.val)
# print (l.val, l.next.val,l.next.next.val)