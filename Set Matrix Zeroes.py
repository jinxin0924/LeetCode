__author__ = 'Xing'
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col,row=set(),set()
        m,n=len(matrix),len(matrix[0])
        for index_m in range(m):
            for index_n in range(n):
                if matrix[index_m][index_n]==0:
                    row.add(index_m)
                    col.add(index_n)
        for index_m in range(m):
            for index_n in range(n):
                if index_m in row or index_n in col:
                    matrix[index_m][index_n]=0

    def setZeroes2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        if(height ==0): return
        width = len(matrix[0])
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    for tmp in range(height):
                        if matrix[tmp][j] != 0:
                            matrix[tmp][j] = 'a'
                    for tmp in range(width):
                        if matrix[i][tmp] != 0:
                            matrix[i][tmp] = 'a'

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0

s=Solution()
# m=[[1,2,3],[4,5,6],[7,8,0]]
m=[[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
s.setZeroes(m)
print(m)
