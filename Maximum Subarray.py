__author__ = 'Xing'
# Find the contiguous subarray within an array
# (containing at least one number) which has the largest sum.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current,max_sum,max_num=0,0,float('-inf')
        for number in nums:
            max_num=max(max_num,number)
            current=current+number if current+number>0 else 0
            max_sum=max(current,max_sum)
        if max_sum==0:
            return max_num
        return max_sum
s=Solution()
test=[[-2,1,-3,4,-1,2,1,-5,4],[-1,-2,-3]]
for p in test:
    print(s.maxSubArray(p))