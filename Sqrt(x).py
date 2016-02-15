__author__ = 'Xing'
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:return None
        if x<1:return 0
        s,e=1,x//2+1
        while s<e-1:
            m=(s+e)//2
            if m*m<x:
                s=m
            elif m*m>x:
                e=m
            else:return m
        return s
s=Solution()
test=[i for i in range(17)]
for case in test:
    print(case,s.mySqrt(case))