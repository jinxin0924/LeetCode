__author__ = 'Xing'
# Given a sorted array and a target value, return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
#
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==1:
            if target<=nums[0]:
                return 0
            else:return 1
        if len(nums)==0:
            return 0
        mid=len(nums)//2
        left,right=0,len(nums)-1
        while left<right-1:
            if nums[mid]<target:
                left=mid
                mid=(right+left)//2
            elif nums[mid]>target:
                right=mid
                mid=(right+left)//2
            else:return mid
        if nums[right]<target:return right+1
        elif nums[left]<target:return right
        else:return left
s=Solution()
print(s.searchInsert([1,3,5,6],5))
print(s.searchInsert([1,3,5,6],2))
print(s.searchInsert([1,3,5,6],7))
print(s.searchInsert([1,3,5,6],0))
print(s.searchInsert([1],1))
print(s.searchInsert([],1))