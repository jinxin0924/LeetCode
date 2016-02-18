__author__ = 'Xing'
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nums=[]
        for i in matrix:
            nums+=i
        return self.search(nums,target)
    def search(self,nums,target):
        if not nums:return False
        mid=len(nums)//2
        if nums[mid]==target:return True
        if nums[mid]<target:return self.search(nums[mid+1:],target)
        if nums[mid]>target:return self.search(nums[:mid],target)

    def searchMatrix2(self, matrix, target):
        l, h = 0, len(matrix) * len(matrix[0]) - 1
        while (l <= h):
            m = l + ((h-l) >> 2)
            v =  matrix[m/len(matrix[0])][m%len(matrix[0])]
            if v < target:
                l = m + 1
            elif v > target:
                h = m - 1
            else:
                return True
        return False


s=Solution()
print(s.searchMatrix([[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]],3))
print(s.searchMatrix([[1]],3))
print(s.searchMatrix([[1,3]],3))
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],30))