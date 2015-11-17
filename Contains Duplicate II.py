__author__ = 'Xing'

# Given an array of integers and an integer k,
# find out whether there are two distinct indices i and j
# in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict_word_index={}
        for index in range(len(nums)):
            if nums[index] not in dict_word_index:
                dict_word_index[nums[index]]=index
            else:
                if (index-dict_word_index[nums[index]])<=k:
                    return True
                else:dict_word_index[nums[index]]=index
        return False
s=Solution()
print(s.containsNearbyDuplicate([1,0,1,1],1))