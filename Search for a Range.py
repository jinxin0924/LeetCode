__author__ = 'Xing'
# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==1:
            if nums[0]==target:
                return [0,0]
            else:return [-1,-1]
        head,end=-1,-1
        left,right=0,len(nums)-1
        mid=len(nums)//2
        while left<=right:
            if nums[mid]<target:
                left=mid+1
                mid=(left+right)//2
            elif nums[mid]>target:
                right=mid-1
                mid=(left+right)//2
            elif nums[mid]==target:
                head=self.left_partition(left,mid,target,nums) #find the head
                end=self.right_partition(mid,right,target,nums) #find the end
                left,right=mid,mid-1  #break the loop
        return [head,end]

    def left_partition(self,left,right,target,nums):
        if right-left<=1:
            if nums[left]==target:
                return left
            else:return right
        mid=(left+right)//2
        if nums[mid]<target:
            left=mid
            return self.left_partition(left,right,target,nums)
        elif nums[mid]==target:
            right=mid
            return self.left_partition(left,right,target,nums)

    def right_partition(self,left,right,target,nums):
        if right-left<=1:
            if nums[right]==target:
                return right
            else:return left
        mid=(left+right)//2
        if nums[mid]>target:
            right=mid
            return self.right_partition(left,right,target,nums)
        elif nums[mid]==target:
            left=mid
            return self.right_partition(left,right,target,nums)

s=Solution()
# print(s.searchRange([5, 7, 7, 8, 8, 10],8))
# print(s.searchRange([0],8))
# print(s.searchRange([2,2],2))
# print(s.searchRange([1],1))
# print(s.searchRange([1,3],1))
print(s.searchRange([1,2,3,3,3,3,4,5,9],3))
print(s.right_partition(4,8,3,[1,2,3,3,3,3,4,5,9]))