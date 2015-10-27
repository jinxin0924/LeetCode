__author__ = 'Xin'
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def partition(nums):
            if len(nums)<=1:return nums,0
            mid=len(nums)//2
            left,numL=partition(nums[:mid])
            right,numR=partition(nums[mid:])
            merge,numM=self.merged(left,right)
            return merge,numM+numL+numR
        return len(nums)-partition(nums)[1],partition(nums)
    def merged(self,left,right):
        if left[-1]==right[0]:return list(set(left+right)),1
        else:return left+right,0

s=Solution()
print(s.removeDuplicates([1,1,2]))
print(s.removeDuplicates([1,1,2,2]))
print(s.removeDuplicates([1,1,2,3,3,3,4]))
print(s.removeDuplicates([1,1,2]))

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:]=[nums[i] for i in range(len(nums)) if nums[i]!=nums[i-1] or i==0]
        return len(nums)
p=Solution()
print(p.removeDuplicates([1,1,2,3,3,3,4]))