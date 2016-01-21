__author__ = 'Xing'
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        result=[]
        n,m,cnt=len(matrix),len(matrix[0]),0
        while len(result)<m*n: #走一圈，4次遍历
            for i in range(cnt,m-cnt):
                result.append(matrix[cnt][i])
            if  len(result)==m*n:
                break
            for j in range(cnt+1,n-cnt):
                result.append(matrix[j][i])
            if  len(result)==m*n:
                break
            for i in range(m-cnt-2,cnt-1,-1):
                result.append(matrix[j][i])
            if  len(result)==m*n:
                break
            for j in range(n-cnt-2,cnt,-1):
                result.append(matrix[j][i])
            cnt+=1
        return result

s=Solution()
print(s.spiralOrder([
[ 1, 2, 3 ],
[ 4, 5, 6 ],
[ 7, 8, 9 ]
]))

print(s.spiralOrder([
[ 1, 2, 3,4 ],
[ 5, 6,7,8],
[ 9,10,11,12]
]))

print(s.spiralOrder([
[ 1, 2, 3,4 ],
[ 5, 6,7,8],
[ 9,10,11,12],
[ 13,14,15,16]
]))

