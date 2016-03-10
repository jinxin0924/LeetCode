__author__ = 'Xing'
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
#
# Example:
# (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
# (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # if len(nums)>1:
        #     for index in range(len(nums)-1):
        #         if index%2==0 and nums[index+1]<nums[index]:
        #             nums[index+1],nums[index]=nums[index],nums[index+1]
        #         if index%2==1 and nums[index+1]>nums[index]:
        #             nums[index+1],nums[index]=nums[index],nums[index+1]
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

testCase=[1,2,2,1,2,1,1,1,1,2,2,2]
# testCase=[1,3,2,2,3,1]
testCase=[4,5,5,6]
s=Solution()
s.wiggleSort(testCase)
print(testCase)