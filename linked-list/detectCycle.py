class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self , head ):
        # write code here
        if head == None or head.next == None:
            return None

        fast = head
        slow = head

        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
            # print (fast.val)
            # print (slow.val)
            # print ("############")

            if fast.val == slow.val:
                slow2 = head
                while slow2.val != slow.val:
                    slow2 = slow2.next
                    slow = slow.next
                    # print (slow2.val)
                    # print (slow.val)

                return slow2

        return None

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)
l1.next.next.next.next.next.next = ListNode(4)

run = Solution()
l =  run.detectCycle(l1)
print (l.val)


