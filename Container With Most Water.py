__author__ = 'JxKing'
# Given n non-negative integers a1, a2, ..., an,
# where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container,
# such that the container contains the most water.

def bf_maxArea( height):
    """
    :type height: List[int]
    :rtype: int
    """
    hmax=0
    for i in range(len(height)-1):
        for j in range(i+1,len(height)):
            hmax=max(min(height[i],height[j]) * (j-i),hmax)

    return hmax

print(bf_maxArea([1,5,6,3,2,1]),bf_maxArea([2,5,3,2,6,1,3,4]),sep='\t')

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
i,j=0,len(height)-1  #从最大开始考虑
    hmax=0
    while i<j:
        if height[i]<height[j]:
            hmax=max(height[i] * (j-i),hmax)
            i+=1
        else:
            hmax=max(height[j]*(j-i),hmax)
            j-=1
    return hmax
print(maxArea([1,5,6,3,2,1]),maxArea([2,5,3,2,6,1,3,4]),sep='\t')

