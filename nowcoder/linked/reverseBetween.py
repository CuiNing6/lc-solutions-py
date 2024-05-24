#coding:utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param m int整型
# @param n int整型
# @return ListNode类
#
class Solution:
    def reverseBetween(self , head , m , n ):
        # write code here
        if head is None:
            return head

        res = ListNode(0)
        res.next = head

        pre = res
        pos = head

        for _ in range(m-1):
            pre = pre.next
            pos = pos.next

        t = pos
        p = pos.next

        for _ in range(n-m):
            temp = p.next
            p.next = t
            t = p
            p = temp

        pre.next = t
        pos.next = p

        return res.next



    def reverse(self, head):
        if head is None:
            return head

        pre = None
        phead = head

        while phead:
            tmp = phead.next
            phead.next = pre
            pre = phead
            phead = tmp

        return pre

    def reverseKGroup(self, head, k):
        if head == None or head.next == None:
            return head

        count = 0
        phead = head

        while phead != None:
            count += 1
            phead = phead.next
            if count >= k:
                break
        if count < k:
            return head
        else:
            pre = None
            start = head
            for _ in range(k):
                temp = head.next
                head.next = pre
                pre = head
                head = temp
            start.next = self.reverseKGroup(head, k)

            return pre

    def delete(self, head, deletenode):
        if deletenode.next == None:
            phead = head
            while phead.next != deletenode:
                phead = phead.next

            phead.next = None
        else:
            next = deletenode.next
            deletenode.val = next.val
            deletenode.next = next.next
            next.next = None

        return head





l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)


# r = Solution().reverse(l1)
# print (r.val,r.next.val,r.next.next.val,r.next.next.next.val,r.next.next.next.next.val)

# r = Solution().reverseBetween(l1,2,4)
# print (r.val,r.next.val,r.next.next.val,r.next.next.next.val,r.next.next.next.next.val)

# r = Solution().reverseKGroup(l1,2)
# print (r.val,r.next.val,r.next.next.val,r.next.next.next.val,r.next.next.next.next.val)

r = Solution().delete(l1,l1)
print (r.val,r.next.val,r.next.next.val,r.next.next.next.val)