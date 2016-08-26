__author__ = 'Xing'
# Sort a linked list in O(n log n) time using constant space complexity.
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #just like merge sort
    # mid: the head
    # mid_pointer: the pointer to mid linked list
    # left: the node whose val is lower than mid
    # right:  the node whose val is bigger than mid

    def sortList(self, head):
        if head==None or head.next==None:
            return head
        mid,left,right,left_pointer,right_pointer=head,None,None,None,None
        n_mid,n_left,n_right=1,0,0
        current=head.next
        mid.next,mid_ponter=None,mid
        while current!=None:
            if current.val<mid.val:
                if left==None:
                    left=current
                    left_pointer=left
                else:
                    left_pointer.next=current
                    left_pointer=left_pointer.next
                n_left+=1
            elif current.val>mid.val:
                if right==None:
                    right=current
                    right_pointer=right
                else:
                    right_pointer.next=current
                    right_pointer=right_pointer.next

                n_right+=1
            elif current.val==mid.val:
                mid_ponter.next=current
                mid_ponter=mid_ponter.next
                n_mid+=1
            current=current.next
        if right_pointer:
            right_pointer.next=None
        if left_pointer:
            left_pointer.next=None
        if n_left>1:
            left=self.sortList(left)
        if n_right>1:
            right=self.sortList(right)
        if left!=None:
            head=left
            while left.next!=None:
                left=left.next
            left.next=mid
        else:
            head=mid
        while n_mid>1:
            mid=mid.next
            n_mid-=1
        mid.next=right
        return head

def input(nums):
    head=ListNode(nums[0])
    current=head
    for number in nums[1:]:
        current.next=ListNode(number)
        current=current.next
    return head
s=Solution()
# result=s.sortList(input([6, 3, 8, 4, 1, 2, 2, 5, 4, 3]))
for i in range(100):
    import random
    p=[random.randint(1,10) for j in range(10)]
    print(p)
    result=s.sortList(input(p))
    while result!=None:
        print(result.val)
        result=result.next

