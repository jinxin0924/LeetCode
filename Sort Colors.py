__author__ = 'Xing'
# Given an array with n objects colored red, white or blue, sort them so that
# objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index1,index2=-1,-1 #pointer for the start points for 1 and 2
        for index in range(len(nums)):
            col=nums[index]
            if col==0:
                if index1>=0 and index2>=0: #need to swap the three numbers
                    nums[index],nums[index1],nums[index2]=2,0,1
                    index1+=1
                    index2+=1
                elif index1>=0:
                    nums[index],nums[index1]=1,0
                    index1+=1
                elif index2>=0:
                    nums[index],nums[index2]=2,0
                    index2+=1
            elif col==1:#need to take care of the initialization for index1
                if index1==-1 and index2>=0:
                    nums[index],nums[index2]=2,1
                    index1=index2
                    index2+=1
                elif index1==-1 and index2==-1:
                    index1=index
                elif index1>=0 and index2>=0:
                    nums[index],nums[index2]=2,1
                    index2+=1
            elif col==2: # the initialization for index2
                if index2==-1:
                    index2=index

            # print(col,nums,index1,index2)
        return nums
import random
s=Solution()
case=[random.randint(0,2) for i in range(random.randint(0,10))]
# case=[0, 0, 0, 1, 1, 1, 1, 2, 0, 1]
print(case)
print(s.sortColors(case))



