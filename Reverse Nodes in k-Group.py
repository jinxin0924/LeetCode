__author__ = 'Xing'
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# You may not alter the values in the nodes, only nodes itself may be changed.
#
# Only constant memory is allowed.
#
# For example,
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        stack,current,count,remain=[],head,0,ListNode('init')
        while current:
            stack.append(current)
            current=current.next
            if len(stack)==k:
                count+=1
                if count==1:
                    head=stack[-1]
                if remain!=ListNode('init'):
                    remain.next=stack[-1]
                for index in range(k-1,0,-1):
                    stack[index].next=stack[index-1]
                    remain=stack[0]
                stack=[]
        if stack:
            remain.next=stack[0]
        else:remain.next=None
        print(head)
        return head

s=Solution()
p1,p2,p3,p4,p5,p6,p7=ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5),ListNode(6),ListNode(7)
p1.next=p2
p2.next=p3
p3.next=p4
p4.next=p5
p5.next=p6
p6.next=p7
# while p1:
#     print(p1.val)
#     p1=p1.next

result=s.reverseKGroup(p1,k=2)
while result:
    print(result.val)
    result=result.next
