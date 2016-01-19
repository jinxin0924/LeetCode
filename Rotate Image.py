__author__ = 'Xing'
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
class Solution(object):
    def rotate2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        dict1={}
        n=len(matrix)
        for i in range(n):
            dict1[i]=[0]*n
        for index1 in range(n):
            for index2 in range(n):
                dict1[index2][n-1-index1]=matrix[index1][index2]
        return [dict1[i] for i in range(n)]

    #modify matrix in-place
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for index1,index2 in [[i,j] for i in range(n//2) for j in range(i,n-1-i)]:
            count,i,j=0,index1,index2
            number=matrix[i][j]
            while count<4:
                number,matrix[j][n-1-i]=matrix[j][n-1-i],number
                count+=1
                i,j=j,n-1-i
        return matrix
 # * 1 2 3     7 8 9     7 4 1
 # * 4 5 6  => 4 5 6  => 8 5 2
 # * 7 8 9     1 2 3     9 6 3
 #  first reverse up to down, then swap the symmetry
s=Solution()
test=[[[1]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],[[1,2],[3,4]],[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]]
for p in test:
    print(s.rotate2(p))
    print(s.rotate(p))

