__author__ = 'Xing'
# Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p_nums=set([i for i in nums if i>0])
        positive=set()
        for number in range(1,len(p_nums)+2):
            positive.add(number)
            if positive-p_nums:
                return number
s=Solution()
# print(s.firstMissingPositive([1,2,0]))
# print(s.firstMissingPositive([3,4,-1,1]))

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        positive=set()
        for number in range(1,len(nums)+2):
            positive.add(number)
            if positive-nums:
                return number

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 1
        nums=set(nums)
        for number in range(1,len(nums)+1):
            if number not in nums:
                return number
print(s.firstMissingPositive([1,2,0]))
print(s.firstMissingPositive([3,4,-1,1]))
print(s.firstMissingPositive([]))