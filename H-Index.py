# Given an array of citations (each citation is a non-negative integer) of a researcher,
# write a function to compute the researcher's h-index.
#
# According to the definition of h-index on Wikipedia:
#  "A scientist has index h if h of his/her N papers have at least h citations each,
#  and the other N − h papers have no more than h citations each."
#
# For example, given citations = [3, 0, 6, 1, 5],
#  which means the researcher has 5 papers in total and each of them had received
#  3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each
# and the remaining two with no more than 3 citations each, his h-index is 3.
__author__ = 'JxKing'

def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    citations.sort()
    n=len(citations)
    for i in range(n,-1,-1):
        left=[j for j in citations if j<i]
        right=[j for j in citations if j>=i]
        if i<=len(right) and i<=n-len(left):
            return i
    return 0
print(hIndex([3,1,2,5,8,6,7]))
print(hIndex([1,2]))
print(hIndex([1,7,9,4]))
print(hIndex([0,0]))
print(hIndex([0]))
print(hIndex([100]))
print(hIndex([0,1]))
print(hIndex([11,15]))
print(hIndex([1]))

print('second solution:')
def hIndex(citations):
    return sum(i < c for i, c in enumerate(sorted(citations, reverse = True)))
print(hIndex([3,1,2,5,8,6,7]))
print(hIndex([1,2]))
print(hIndex([1,7,9,4]))
print(hIndex([0,0]))
print(hIndex([0]))
print(hIndex([100]))
print(hIndex([0,1]))
print(hIndex([11,15]))
print(hIndex([1]))

