__author__ = 'Xing'
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        current=[root]
        ans=[]
        while current:
            print([i.val for i in current])
            ans.append(current[-1].val)
            next=[]
            for node in current:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            current=next[:]
        return ans
a1=TreeNode(1)
a2=TreeNode(2)
a3=TreeNode(3)
a4=TreeNode(4)
a5=TreeNode(5)
a1.left=a2
a1.right=a3
a2.right=a5
a3.right=a4
s=Solution()
print(s.rightSideView(a1))