__author__ = 'Xing'
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n>=0:
            if n==0:return 1
            if n==1:return x
            if n%2==1:return x*self.myPow(x*x,n>>1)
            else:return self.myPow(x*x,n>>1)
        else:
            n=abs(n)
            if n==0:return 1
            if n==1:return 1/x
            if n%2==1:return 1/x*1/self.myPow(x*x,n>>1)
            else:return 1/self.myPow(x*x,n>>1)
s=Solution()
print(s.myPow(2,2))
print(s.myPow(2,-2))