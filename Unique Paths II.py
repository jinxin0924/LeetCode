__author__ = 'Xing'
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
from functools import wraps
def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1:return 0
        obstacleGrid=tuple([tuple(i) for i in obstacleGrid])
        return self.recurs(obstacleGrid)
    @memo
    def recurs(self,grid):
        m,n=len(grid[0]),len(grid)
        if m==1:
            if 1 not in [i[0] for i in grid]:return 1
            else:return 0
        if n==1:
            if 1 not in grid[0]:return 1
            else:return 0
        right,down=grid[0][1],grid[1][0]
        if right==0 and down==0:
            return self.recurs(tuple([i[1:] for i in grid]))+self.recurs(grid[1:])
        elif right==0 and down==1:
            return self.recurs(tuple([i[1:] for i in grid]))
        elif right==1 and down==0:
            return self.recurs(grid[1:])
        else:
            return 0


    def uniquePathsWithObstacles2(self, grid):
        if grid[0][0]==1:return 0
        m,n=len(grid[0]),len(grid)
        dp=[[0]*(m+1) for i in range(n+1)]
        dp[0][1]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if grid[i-1][j-1]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
s=Solution()
test=[[[0,0,0],[0,1,0],[0,0,0]],[[0],[1]],[[0,1]],[[1,0],[0,0]],[[0,1,0],[0,0,0]]]
# test=[[[0,1,0],[0,0,0]]]
for p in test:
    print(s.uniquePathsWithObstacles(p),s.uniquePathsWithObstacles2(p))
