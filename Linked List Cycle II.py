__author__ = 'Xing'
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# Note: Do not modify the linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow2=head
                while slow2 is not slow:
                    slow=slow.next
                    slow2=slow2.next
                return slow
        return None

a0=ListNode(0)
a1=ListNode(1)
a2=ListNode(2)
a3=ListNode(3)
a4=ListNode(4)
a5=ListNode(5)
a0.next=a1
a1.next=a2
a2.next=a3
a3.next=a4
a4.next=a5
a5.next=None

s=Solution()
print(s.detectCycle(a0))
