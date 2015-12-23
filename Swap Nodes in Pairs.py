__author__ = 'Xing'
# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNodeListNode(1)
        :rtype: ListNode
        """
        a=head
        b=a.next
        if not b:
            return a
        c=b.next
        head=b
        if not c:
            b

a,b,c,d=ListNode(1),ListNode(2),ListNode(3),ListNode(4)
a.next=b
b.next=c
c.next=d
# while a:
#     print(a.val)
#     a=a.next
s=Solution()
p=s.swapPairs(a)
while p:
    print(p.val)
    p=p.next