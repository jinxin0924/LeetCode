__author__ = 'JxKing'
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number,
# target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
        nums.sort()
        best=1000
        best_sum=0
        if len(nums)<3:
            return 0
        for first in range(len(nums)-2):
            second,third=first+1,len(nums)-1
            while second<third:
                cur=nums[first]+nums[second]+nums[third]
                if best>abs(target-cur):
                    best=abs(target-cur)
                    best_sum=cur
                if target-cur>0:
                    second+=1
                elif target-cur<0:
                    third-=1
                elif target==cur:
                    return cur
        return best_sum
print(threeSumClosest([-1,2,1,-4],1))
print(threeSumClosest([0,0,0],1))
print(threeSumClosest([0,1,2],3))
print(threeSumClosest([0,1,2,-3],1))