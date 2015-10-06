__author__ = 'JxKing'
# Follow up for H-Index:
# What if the citations array is sorted in ascending order? Could you optimize your algorithm?
# Hint:
#   Expected runtime complexity is in O(log n) and the input is sorted.

def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    n=len(citations)
    low=0
    high=n-1
    m=(high+low)//2
    while low<=high:
        if n-1-m<citations[m]:
            high=m-1
            m=(high+low)//2
        if n-1-m>=citations[m]:
            low=m+1
            m=(high+low)//2
    return (n-low)
print(hIndex([3,1,2,5,8,6,7]))
print(hIndex([1,2]))
print(hIndex([1,7,9,4]))
print(hIndex([0,0]))
print(hIndex([0]))
print(hIndex([100]))
print(hIndex([0,1]))
print(hIndex([11,15]))
print(hIndex([1]))
