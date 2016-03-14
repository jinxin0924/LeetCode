__author__ = 'Xing'
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# For example,
# If n = 4 and k = 2, a solution is:
#
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result=[]
        for number in range(1,n+1):
            self.recursion([number],number,n,result,k-1)
        return result
    def recursion(self,part,start,n,result,k):
        if k==0:
            result.append(part)
            return
        if start<n:
            for number in range(start+1,n+1):
                self.recursion(part+[number],number,n,result,k-1)

    def combine2(self,n,k):
        result=[]
        stack=[[[],0,k]]
        while stack:
            p=stack.pop()
            current,start,count=p[0],p[1],p[2]
            if count==0:
                result.append(current)
                continue
            if start<n:
                for number in range(start+1,n+1):
                    stack.append([current+[number],number,count-1])
        return result

s=Solution()
print(s.combine(4,2))
print(s.combine2(4,2))