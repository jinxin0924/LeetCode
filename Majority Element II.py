__author__ = 'Xing'
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# The algorithm should run in linear time and in O(1) space.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<2:
            return nums
        c1,c2=0,0
        n1,n2=None,None
        for number in nums:
            if c1==0 and number!=n2:
                n1,c1=number,1
            elif c2==0 and number!=n1:
                n2,c2=number,1
            elif number==n1:
                c1+=1
            elif number==n2:
                c2+=1
            else:
                c1-=1
                c2-=1
        size = len(nums)
        return [n for n in (n1, n2)
                   if n is not None and nums.count(n) > size / 3]
        # ans=[]
        # count=1
        # major=nums[0]
        # for number in nums[1:]:
        #     if count==0:
        #         major=number
        #         count=2
        #     else:
        #         if number==major:
        #             count+=2
        #         else:
        #             count-=1
        # return major

s=Solution()
print(s.majorityElement([3,2,3]))
print(s.majorityElement([3,2]))
print(s.majorityElement([6,5,5]))
print(s.majorityElement([5,6,5]))
print(s.majorityElement([2,2,9,3,9,3,9,3,9,3,9,3,9,3,9,3,9]))