__author__ = 'Xing'

# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
#
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
# It doesn't matter what you leave beyond the new length.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count,length=0,0
        pre='1'
        for number in nums:
            if number!=pre:
                count,pre=1,number
                length+=1
            elif number==pre:
                count+=1
                if count<=2:
                    length+=1
            print(number,length)
        return length

    def remove2(self,nums):
        if not nums: return 0
        newLength = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]: # different than prevous one
                nums[newLength] = nums[i]
                newLength += 1
                count = 1
            elif count == 1: # differ from the previous but no more than two
                nums[newLength] = nums[i]
                newLength += 1
                count += 1

        return newLength


s=Solution()
print(s.removeDuplicates([1,1,1,2,2,3]))
print(s.removeDuplicates([]))
