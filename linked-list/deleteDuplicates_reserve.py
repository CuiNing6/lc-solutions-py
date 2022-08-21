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

        fast = head

        while fast!=None:
            while fast.next!=None and fast.next.val == fast.val:
                fast.next = fast.next.next

            fast = fast.next

        return head

l1 = ListNode(1)
l1.next = ListNode(5)
l1.next.next = ListNode(5)
l1.next.next.next = ListNode(7)

l2 = ListNode(1)
l2.next = ListNode(1)
l2.next.next = ListNode(1)

run = Solution()
l =  run.deleteDuplicates(l2)
print (l.val)
# print (l.val, l.next.val,l.next.next.val)

