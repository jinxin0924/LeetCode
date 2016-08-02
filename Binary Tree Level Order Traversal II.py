__author__ = 'Xing'
# Given a binary tree, return the bottom-up level order traversal of its nodes
# ' values. (ie, from left to right, level by level from leaf to root).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack=[[root]]
        ans=[]
        while stack:
            current=stack.pop()
            ans+=[[i.val for i in current]]

            nextList=[]
            for node in current:
                if node.left:
                    nextList.append(node.left)
                if node.right:
                    nextList.append(node.right)
            if nextList:
                stack.append(nextList)
        ans.reverse()
        return ans

s=Solution()

a1=TreeNode(3)
a2=TreeNode(9)
a3=TreeNode(20)
a4=TreeNode(15)
a5=TreeNode(7)

a1.left=a2
a1.right=a3
a3.left=a4
a3.right=a5

print(s.levelOrderBottom(a1))