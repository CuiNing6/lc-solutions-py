

def rank_link(head):
    if head is None or head.next is None:
        return None

    cur = head.next

    while cur.next is not None:
        tmp = cur.next
        if tmp.val > cur.val:
            cur.next = reserve(head)

    return cur


def reserve(head):
    if head is None or head.next is None:
        return head

    pre = head
    cur = head.next
    next = cur.next
    pre.next = None

    while cur.next is not None:
        cur.next = pre
        pre = cur
        cur = next
        next = cur.next

    cur.next = pre

    return cur