__author__ = 'Xing'
# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
# Note that there may be more than one LIS combination, it is only necessary for you to return the length.
#
# Your algorithm should run in O(n2) complexity.


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        if length<=1:
            return length
        dp=[0]*length
        dp[0]=1
        for end in range(1,length):
            cur_length=1
            for index in range(end):
                if nums[index]<nums[end]:
                    cur_length=max(cur_length,dp[index]+1)
            dp[end]=cur_length
        return max(dp)

    def lengthOfLIS2(self, nums):
        def search(temp, left, right, target):
            if left == right:
                return left
            mid = left+(right-left)//2
            return search(temp, mid+1, right, target) if temp[mid]<target else search(temp, left, mid, target)
        temp = []
        for num in nums:
            pos = search(temp, 0, len(temp), num)
            if pos >=len(temp):
                temp.append(num)
            else:
                temp[pos]=num
            print(temp)
        return len(temp)

s=Solution()
# print(s.lengthOfLIS([10,9]))
# print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
# print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS2([2, 5, 3, 4]))
# print(s.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))