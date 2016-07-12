__author__ = 'Xing'
# Given two arrays of length m and n with digits 0-9 representing two numbers.
# Create the maximum number of length k <= m + n from digits of the two.
# The relative order of the digits from the same array must be preserved.
#  Return an array of the k digits. You should try to optimize your time and space complexity.
# Example 1:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# return [9, 8, 6, 5, 3]
#
# Example 2:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# return [6, 7, 6, 0, 4]

class Solution(object):

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def maxList(nums,k):
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def merge(nums1,nums2):
            return [max(nums1,nums2).pop(0) for _ in nums1+nums2]
            # return [max(a, b).pop(0) for _ in a+b]

        return max(merge(maxList(nums1, i), maxList(nums2, k-i))
               for i in range(k+1)
               if i <= len(nums1) and k-i <= len(nums2))

s=Solution()
print(s.maxNumber([3, 4, 6, 5],[9, 1, 2, 5, 8, 3],5))
# print(s.maxNumber([6,7],[6,0,4],5))
# print(s.maxNumber([3,9],[8,9],3))
# print(s.maxNumber([6,6,8],[5,0,9],3))
# print(s.maxNumber([3,4,6,5],[9,1,2,5,8,3],5))
# print(s.maxList([6,6,8],2))
# print(s.maxList([9,1,2,5,8,3],3))
def test():
    import random
    n=random.randint(0,5)
    m=random.randint(0,5)
    k=random.randint(0,n+m)
    nums1=[random.randint(0,9) for i in range(n)]
    nums2=[random.randint(0,9) for i in range(m)]
    print(nums1,nums2,k,s.maxNumber(nums1,nums2,k))

