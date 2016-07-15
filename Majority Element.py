__author__ = 'Xing'
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=1
        major=nums[0]
        for number in nums[1:]:
            if count==0:
                major=number
                count=1
            else:
                if number==major:
                    count+=1
                else:
                    count-=1
        return major
s=Solution()
print(s.majorityElement([1]))
print(s.majorityElement([1,2,1,2,1,3,3,3,3,3,3]))
print(s.majorityElement([6,5,5]))