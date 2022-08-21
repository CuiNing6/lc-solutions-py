class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
class Solution:
    def reorderList(self , head ):
        # write code here
        if head is None or head.next is None:
            return head

        fast = head.next
        slow = head

        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next

        tail = slow.next
        slow.next = None
        tmp = None

        while tail!=None:
            next = tail.next
            tail.next = tmp
            tmp = tail
            tail = next

        res = head
        while res!=None and tmp!=None:
            res_tmp = tmp.next
            tmp.next = res.next
            res.next = tmp
            res = res.next.next
            tmp = res_tmp

        return head

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

run = Solution()
l =  run.reorderList(l1)
print (l.val,l.next.val,l.next.next.val, l.next.next.next.val, l.next.next.next.next.val)





