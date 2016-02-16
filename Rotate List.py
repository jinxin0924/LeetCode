__author__ = 'Xing'
# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:return head
        nodeList=[]
        pre=head
        while head:
            nodeList.append(head)
            head=head.next
        k=k%len(nodeList)
        if len(nodeList)<=1:return pre
        nodeList[-1].next=nodeList[0]
        nodeList[-k-1].next=None
        return nodeList[-k]


s=Solution()
a1=ListNode(1)
a2=ListNode(2)
a3=ListNode(3)
a4=ListNode(4)
a5=ListNode(5)
# a1.next=a2
# a2.next=a3
# a3.next=a4
# a4.next=a5
# a5.next='NULL'

a1.next=a2
a2.next=None


def printlistnode(head):
    while head:
        print(head.val)
        head=head.next
printlistnode(a1)
print()
printlistnode(s.rotateRight(a1,3))