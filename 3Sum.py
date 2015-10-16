__author__ = 'JxKing'
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
# The solution set must not contain duplicate triplets.
#     For example, given array S = {-1 0 1 2 -1 -4},
#
#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)

def threeSum1(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    left=[] #记录负数
    right=[] #记录正数
    middle=[] #记录0
    result=[] #记录答案
    for num in nums:
        if num==0:
            middle.append(num)
        elif num>0:
            right.append(num)
        else:
            left.append(num)
    if len(middle)<3:
        if len(left)==0 or len(right)==0: #如果0的个数少于3并且没有正数或者没有负数，无解
            return []
    else:
        result.append([0,0,0])
    if len(middle)>0:
        for i in left:
            if -i in right:
                if [i,0,-i] not in result:
                    result.append([i,0,-i])
    if len(left)>=2:
        for i in range(len(left)-1):
            for j in range(i+1,len(left)):
                if -(left[i]+left[j]) in right:
                    p=[min(left[i],left[j]),max(left[i],left[j]),-(left[i]+left[j])]
                    if p not in result:
                        result.append(p)
    if len(right)>=2:
        for i in range(len(right)-1):
            for j in range(i+1,len(right)):
                if -(right[i]+right[j]) in left:
                    p=[-(right[i]+right[j]),min(right[i],right[j]),max(right[i],right[j])]
                    if p not in result:
                        result.append(p)
    return result
print(threeSum1([-1, 0, 1, 2, -1, -4]))

print(threeSum1([-1,3,-2]))
print(threeSum1([1,1,-2]))

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    result=[]
    length=len(nums)
    for i in range(length-2):
        first=nums[i]
        if first>0:
            break
        s,t=i+1,length-1
        while s<t:
            second,third=nums[s],nums[t]
            if first+second+third==0:
                t-=1
                if [first,second,third] not in result:
                    result.append([first,second,third])
            elif first+second+third>0:
                t-=1
            elif first+second+third<0:
                s+=1
    return result
print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([-1,3,-2]))
print(threeSum([1,1,-2]))
print(threeSum([0,0,0,0]))
