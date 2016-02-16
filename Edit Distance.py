__author__ = 'Xing'
# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
#  (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
# a) Insert a character
# b) Delete a character
# c) Replace a character

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n,m=len(word1),len(word2)
        if n>m:
            n,m=m,n
            word1,word2=word2,word1
        if n==0:return m
        dp=[[0]*(m+1) for i in range(n+1)]
        for i in range(1,n+1):
            dp[i][0]=i
        for i in range(1,m+1):
            dp[0][i]=i
        for i in range(1,n+1):
            for j in range(1,m+1):
                dp[i][j]=dp[i-1][j-1]+1
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                # dp[i][j]=min(dp[i-1][j]+1,dp[i][j])
                # dp[i][j]=min(dp[i][j-1]+1,dp[i][j])
                dp[i][j]=min([dp[i-1][j]+1,dp[i][j-1]+1,dp[i][j]])
        # print(dp)
        return dp[-1][-1]
s=Solution()
# print(s.minDistance('abc','ac')) #insert
# print(s.minDistance('ab','ac')) #replace
# print(s.minDistance('a','ac'))  #delete
# print(s.minDistance('a','ca'))
# print(s.minDistance('','ca'))
# print(s.minDistance('',''))
# print(s.minDistance('se','a'))
# print(s.minDistance('sea','ate'))
print(s.minDistance('algorithm','altruistic'))
