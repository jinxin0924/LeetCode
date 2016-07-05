__author__ = 'Xing'
#https://leetcode.com/problems/rectangle-area/
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        overlap=max(min(C,G) - max(A,E),0) * max(min(D,H)-max(F,B),0)

        return (C-A)*(D-B)+(G-E)*(H-F)-overlap


s=Solution()
# print(s.computeArea(-3,0,3,4,0,-1,9,2))
print(s.computeArea(-2,-2,2,2,-2,-2,2,2))
# print(s.computeArea(0,0,0,0,-1,-1,1,1))
