__author__ = 'Xing'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """



a1=TreeNode(1)
a2=TreeNode(2)
a3=TreeNode(2)
a4=TreeNode(3)
a5=TreeNode(3)

a1.left=a2
a1.right=a3
a2.right=a4
a3.right=a5

s=Solution()
print(s.isSymmetric(a1))

