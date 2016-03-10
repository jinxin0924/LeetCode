__author__ = 'Xing'
# Sort a linked list in O(n log n) time using constant space complexity.
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):

