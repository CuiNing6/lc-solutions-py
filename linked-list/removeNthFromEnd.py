class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
class Solution:
    def removeNthFromEnd(self , head , n ):
        # write code here
        if head == None or head.next == None:
            return None

        fast = head
        slow = head
        tmp = head

        for i in range(1,n):
            fast = fast.next

        while fast.next!=None:
            fast = fast.next
            tmp = slow
            slow = slow.next

        if slow!=head:
            tar = tmp.next
            tmp.next = tar.next
        else:
            head = head.next

        return head

l1 = ListNode(1)
l1.next = ListNode(5)
l1.next.next = ListNode(7)

run = Solution()
l =  run.removeNthFromEnd(l1,2)
print (l.val, l.next.val)
# print (l.val)