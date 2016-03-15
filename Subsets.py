__author__ = 'Xing'
# Given a set of distinct integers, nums, return all possible subsets.
#
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If nums = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        if n<1:return []
        nums.sort()
        dp=[[] for i in range(n)]
        dp[0]=[[],[nums[0]]]
        for index in range(1,n):
            for part in dp[index-1]:
                dp[index].append(part)
                dp[index].append(part+[nums[index]])
        return dp[-1]

s=Solution()
print(s.subsets([1,2,3,4]))


