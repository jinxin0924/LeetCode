__author__ = 'Xing'
# Given an array of integers, find out whether there are two distinct indices i and j in the array
# such that the difference between nums[i] and nums[j] is at most t and the difference
# between i and j is at most k.

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums)<=k:
            nums.sort()
            for first in range(len(nums)-1):
                for second in range(first+1,len(nums)):
                    if abs(nums[first-second])<=t:
                        return True
            return  False
        if len(set(nums))!=len(nums): #NO same value
            return True
        current_list=nums[:k].copy()
        current_list.sort()
        dict1={}
        index_index={}# record the nums index to the new list's index
        for i in range(k):
            dict1[nums[i]]=i
        for index in range(k):
            index_index[dict1[current_list[index]]]=index
        for first in range(k-1):
            for second in range(first+1,k):
                if abs(current_list[first-second])<=t:
                    return True
        for index in range(k,len(nums)):
            current_index=index_index[index-k]
            current_list[]=nums[index]
