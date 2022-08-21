class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
class Solution:
    def hasCycle(self , head ):
        # write code here
        if head is None or head.next is None:
            return False

        fast = head
        slow = head

        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next

            if fast.val == slow.val:
                return True

        return False

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)
l1.next.next.next.next.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)

run = Solution()
l =  run.hasCycle(l1)
print (l)