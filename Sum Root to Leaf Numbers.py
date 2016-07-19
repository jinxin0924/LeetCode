__author__ = 'Xing'
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans=[]
        if not root:
            return 0
        stack=[[root]]
        while stack:
            current=stack.pop()
            if current[-1].left==None and current[-1].right==None:
                p=0
                for i in range(len(current)):
                    p+=current[i].val*10**(len(current)-1-i)
                ans.append(p)
            if current[-1].left!=None:
                stack.append(current+[current[-1].left])
            if current[-1].right !=None:
                stack.append(current+[current[-1].right])
        return sum(ans)
s=Solution()

a1=TreeNode(1)
a2=TreeNode(2)
a3=TreeNode(3)
a1.left=a2
a1.right=a3
print(s.sumNumbers(a1))