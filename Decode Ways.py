__author__ = 'Xing'
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n=len(s)
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            if s[i-1]!='0':
                dp[i]+=dp[i-1]
            if i>1 and 9<int(s[i-2:i])<=26:
                dp[i]+=dp[i-2]
        return dp[-1]


s=Solution()
# print(s.numDecodings('123'))
print(s.numDecodings('00'))
