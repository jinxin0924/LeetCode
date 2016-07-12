__author__ = 'Xing'
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
# ["1->2->5", "1->3"]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root==None:
            return []
        stack=[[root]]
        ans=[]
        while stack:
            current=stack.pop()
            if current[-1].left:
                stack.append(current+[current[-1].left])
            if current[-1].right:
                stack.append(current+[current[-1].right])
            if current[-1].left==None and current[-1].right==None:
                ans.append('->'.join([str(node.val) for node in current]))
        return ans