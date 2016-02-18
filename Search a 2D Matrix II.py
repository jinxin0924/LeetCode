__author__ = 'Xing'
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:return False
        result=[]
        self.search(matrix,target,result)
        # print(result)
        if sum(result):
            return True
        return False
    def search(self,matrix,target,result):
        # print(matrix)
        n=len(matrix)
        if n==0:
            result.append(0)
            return
        m=len(matrix[0])
        if m==0:
            result.append(0)
            return
        # print('nm',n,m)
        mid_n,mid_m=n//2,m//2
        # print('nm/2',mid_m,mid_n)
        # print(matrix[mid_n][mid_m])
        if matrix[mid_n][mid_m]==target:
            result.append(1)
            return
        elif matrix[mid_n][mid_m]<target:
            self.search(matrix[mid_n+1:],target,result)
            self.search([[matrix[j][i] for i in range(mid_m+1,m)] for j in range(mid_n+1)],target,result)
        elif matrix[mid_n][mid_m]>target:
            self.search(matrix[:mid_n],target,result)
            self.search([[matrix[j][i] for i in range(mid_m)] for j in range(mid_n,n)],target,result)

    def searchMatrix2(self, matrix, target):
        if not matrix:return False
        stack=[matrix]
        while stack:
            matrix=stack.pop()
            try:
                n,m=len(matrix),len(matrix[0])
                mid_n,mid_m=n//2,m//2
                if matrix[mid_n][mid_m]==target:
                    return True
                elif matrix[mid_n][mid_m]<target:
                    stack.append(matrix[mid_n+1:])
                    stack.append([[matrix[j][i] for i in range(mid_m+1,m)] for j in range(mid_n+1)])
                elif matrix[mid_n][mid_m]>target:
                    stack.append(matrix[:mid_n])
                    stack.append([[matrix[j][i] for i in range(mid_m)] for j in range(mid_n,n)])
            except:pass
        return False
    def searchMatrix3(self, matrix, target):
        j = -1
        for row in matrix:
            while j + len(row) and row[j] > target:
                j -= 1
            if row[j] == target:
                return True
        return False
s=Solution()
print(s.searchMatrix([[1,4,7, 11, 15],[2,   5,  8, 12, 19],[3,   6,  9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]],20))
print(s.searchMatrix2([[1,4,7, 11, 15],[2,   5,  8, 12, 19],[3,   6,  9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]],20))
print(s.searchMatrix([[1,4,7, 11, 15],[2,   5,  8, 12, 19],[3,   6,  9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]],5))
print(s.searchMatrix2([[1,4,7, 11, 15],[2,   5,  8, 12, 19],[3,   6,  9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]],5))
