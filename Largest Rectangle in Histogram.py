__author__ = 'Xing'
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights)==0:return 0
        if len(heights)==1:return heights[0]
        MinIndex=self.findMinIndex(heights)
        length=len(heights)
        return max(heights[MinIndex]*length,self.largestRectangleArea(heights[:MinIndex]),self.largestRectangleArea(heights[min(MinIndex+1,length-1):]))

    def findMinIndex(self,nums):
        index,minimum=0,nums[0]
        for i in range(1,len(nums)):
            if nums[i]<minimum:
                index,minimum=i,nums[i]
        return index

# s=Solution()
# print(s.largestRectangleArea([2,1,5,6,2,3]))


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """




