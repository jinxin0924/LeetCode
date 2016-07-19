__author__ = 'Xing'
# Given an array of n integers where n > 1, nums, return an array output such that
# output[i] is equal to the product of all the elements of nums except nums[i].
#
# Solve it without division and in O(n).
#
# For example, given [1,2,3,4], return [24,12,8,6].
#
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        current=1
        output=[]
        for index in range(n):
            output.append(current)
            current*=nums[index]
        current=1
        for index in range(n-1,-1,-1):
            output[index]*=current
            current*=nums[index]
        return output
s=Solution()
print(s.productExceptSelf([1,2,3,4]))