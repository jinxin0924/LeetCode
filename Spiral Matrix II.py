__author__ = 'Xing'
# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#  [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result=[[0 for i in range(n)] for j in range(n)]
        number,cnt=1,0
        while number<=n**2:
            for i in range(cnt,n-cnt):
                result[cnt][i]=number
                number+=1
            if number>n**2:break
            for j in range(cnt+1,n-cnt):
                result[j][i]=number
                number+=1
            if number>n**2:break
            for i in range(n-cnt-2,cnt-1,-1):
                result[j][i]=number
                number+=1
            if number>n**2:break
            for j in range(n-cnt-2,cnt,-1):
                result[j][i]=number
                number+=1
            cnt+=1
        return result

s=Solution()
test=[1,2,3,4]
for p in test:
    print(s.generateMatrix(p))
