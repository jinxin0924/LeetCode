__author__ = 'JxKing'

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

def bf_findMedianSortedArrays(nums1, nums2): #合并之后取中间值
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    merge=[]
    i,j=0,0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            merge.append(nums1[i])
            i+=1
        else:
            merge.append(nums2[j])
            j+=1
    merge+=nums1[i:]
    merge+=nums2[j:]
    n=len(merge)
    if n%2==0:
        return (merge[n//2]+merge[n//2-1])/2
    else:
        return merge[n//2]

print(bf_findMedianSortedArrays([0,1,2,3],[1,4,5,6,7,9]))

# def findMedianSortedArrays(nums1, nums2):

