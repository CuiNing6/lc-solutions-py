class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self , pHead , k ):
        # write code here
        if pHead is None:
            return None

        fast = pHead
        slow = pHead

        for i in range(k):
            if fast==None:
                return None
            fast = fast.next

        while fast!=None:
            fast = fast.next
            slow = slow.next

        return slow


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
# l1.next.next.next.next.next = ListNode(6)
# l1.next.next.next.next.next.next = ListNode(7)

run = Solution()
l =  run.FindKthToTail(l1,2)
print (l.val)