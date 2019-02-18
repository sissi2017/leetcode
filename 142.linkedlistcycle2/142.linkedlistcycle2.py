i# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return None
        p1=p2=head
        while p1.next and p2.next.next:
            p1=p1.next
            p2=p2.next.next
            if p1 == p2:
                p = head
                while p!=p1:
                    p=p.next
                    p1=p1.next
                return p
        return None
