__author__ = 'Xing'
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You must do this in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse(self,head):
        last=None
        while head:
            curr=head
            head=head.next
            curr.next=last
            last=curr
        return last
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:return
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        re_slow=self.reverse(slow)
        curr1,curr2=head,re_slow
        while curr1 and curr2:
            next1=curr1.next
            curr1.next=curr2
            next2=curr2.next
            curr2.next=next1
            curr1=next1
            curr2=next2



