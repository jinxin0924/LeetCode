__author__ = 'Xing'
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path
# from the root node down to the nearest leaf node.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth,stack=0,[root]
        while stack:
            depth+=1
            next=[]
            while stack:
                curr=stack.pop()
                if curr.left is None and curr.right is None:
                    return depth
                elif curr.left is not None:
                    next.append(curr.left)
                if curr.right is not None:
                    next.append(curr.right)
            stack=next

a1=TreeNode(1)
a2=TreeNode(2)
a3=TreeNode(3)
a4=TreeNode(4)
a1.left=a2
a2.left=a4
a1.right=a3
s=Solution()
print(s.minDepth(a1))
