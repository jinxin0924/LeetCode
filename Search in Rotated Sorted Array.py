__author__ = 'Xing'
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.

class Solution(object):
    def search(self, nums, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #2分法，逻辑一一理顺
        if not nums:return -1
        s,e=0,len(nums)-1
        while s<=e:
            m=s+(e-s)//2
            # print(s,e,m)
            if nums[e]==t:return e
            if nums[s]==t:return s
            if nums[m]==t:return m
            if nums[s]==nums[e]:return  -1
            elif nums[s]>nums[e]:
                if nums[m]>=nums[s]:
                    if t>nums[m]:
                        s=m+1
                    else:
                        if nums[s]<t:
                            e=m-1
                        else:s=m+1
                else:
                    if t>nums[m]:
                        if t>nums[s]:e=m-1
                        else:s=m+1
                    else:
                        e=m-1
            elif nums[s]<nums[e]:
                if nums[m]>t:
                    e=m-1
                else:
                    s=m+1
        return -1





s=Solution()
print(s.search([4,5,6,7,0,1,2],7))
print(s.search([0],7))
print(s.search([1,3],4))
print(s.search([3,1],4))
print(s.search([5,1,3],6))
print(s.search([1,2,3,4,5,6],4))
print(s.search([1],1))