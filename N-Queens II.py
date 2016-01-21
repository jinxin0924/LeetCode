__author__ = 'Xing'
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        result=[0]
        for index in range(n):
            self.queen([index],set([index]),set([index]),result,n)
        return result[0]
    def queen(self,current,xy_sum,xy_diff,result,n):
        p=len(current)
        if p==n:
            result[0]+=1
            return
        for q in range(n):
            if q not in current and p+q not in xy_sum and q-p not in xy_diff:
                self.queen(current+[q],xy_sum|set([p+q]),xy_diff|set([q-p]),result,n)

s=Solution()
print(s.totalNQueens(9))