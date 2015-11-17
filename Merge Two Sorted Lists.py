__author__ = 'Xing'
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
#  the nodes of the first two lists.
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1Pointer, l2Pointer = l1, l2
        if l1 and l2:
            if l1.val > l2.val:
                newList = ListNode(l2.val)
                l2Pointer = l2.next
            else:
                newList = ListNode(l1.val)
                l1Pointer = l1.next
        elif not l1:
            newList=l2
            return newList
        elif not l2:
            newList=l1
            return newList
        current=newList
        while l1Pointer and l2Pointer:
            if l1Pointer.val>l2Pointer.val:
                current.next=l2Pointer
                l2Pointer=l2Pointer.next
                current=current.next
            else:
                current.next=l1Pointer
                l1Pointer=l1Pointer.next
                current=current.next
        if l1Pointer:
            current.next=l1Pointer
        else:
            current.next=l2Pointer
        return newList