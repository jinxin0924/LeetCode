__author__ = 'Xing'
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# For example:
# A = [2,3,1,1,4], return true.
#
# A = [3,2,1,0,4], return false.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        max_step,index,length=nums[0],0,len(nums)
        while index<length-1 and index<max_step:
            index+=1
            max_step=max(nums[index]+index,max_step)
        if max_step>=length-1:
            return True
        return False

s=Solution()
test=[[2,3,1,1,4],[3,2,1,0,4],[1,2],[1,0,3],[0],[0,1],[2,0,0]]
# test=[[0]]
for p in test:
    print(s.canJump(p))