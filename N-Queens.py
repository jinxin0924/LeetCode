__author__ = 'Xing'
# The n-queens puzzle is the problem of placing n queens
# on an n×n chessboard such that no two queens attack each other.
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result=[]
        for index in range(n):
            self.queen([index],set([index]),set([index]),result,n)
        return result
    def queen(self,current,xy_sum,xy_diff,result,n):
        p=len(current)
        if p==n:
            result.append([''.join(['Q' if i==index else '.' for i in range(n)]) for index in current])
            return
        for q in range(n):
            if q not in current and p+q not in xy_sum and q-p not in xy_diff:
                self.queen(current+[q],xy_sum|set([p+q]),xy_diff|set([q-p]),result,n)

s=Solution()
print(s.solveNQueens(9))