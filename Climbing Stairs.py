__author__ = 'Xing'
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:return 1
        dp=[0 for i in range(n+1)]
        dp[0],dp[1]=1,1
        for step in range(2,n+1):
            dp[step]=dp[step-1]+dp[step-2]
        return dp[-1]
s=Solution()
test=[1,2,3,4,5,6]
for case in test:
    print(s.climbStairs(case))