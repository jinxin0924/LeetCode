__author__ = 'Xing'
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n=len(grid[0]),len(grid)
        dp=[[0]*(m) for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    dp[0][0]=grid[0][0]
                elif i==0 and j>0:
                    dp[i][j]=dp[i][j-1]+grid[i][j]
                elif j==0 and i>0:
                    dp[i][j]=dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j]+grid[i][j],dp[i][j-1]+grid[i][j])
        return dp[-1][-1]

s=Solution()
print(s.minPathSum([[1,2],[1,1]]))
print(s.minPathSum([[1,2,3],[4,5,6]]))