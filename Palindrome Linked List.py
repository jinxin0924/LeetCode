__author__ = 'Xing'
# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow,fast=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        node=None
        while slow:
            nxt=slow.next
            slow.next=node
            node=slow
            slow=nxt
        while node:
            if node.val !=head.val:
                return False
            node=node.next
            head=head.next
        return True




