__author__ = 'JxKing'
# Write a function to find the longest common prefix string amongst an array of strings.

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs)==0:
        return ''
    if len(strs)==1:
        return strs[0]
    strs.sort()
    current=strs[0]
    for j in strs[1:]:
        if len(j)<len(current):
            current=current[:len(j)]
        while 0<len(current) and current!=j[:len(current)]:
            current=current[:-1]
    return current

print(longestCommonPrefix(['a','aa','aaaa','aac']))
print(longestCommonPrefix(['aaa','aa','aaaa','aac']))
print(longestCommonPrefix(['ca','a']))
print(longestCommonPrefix(["a","a","b"]))
print(longestCommonPrefix(['aac','ab']))


def longestCommonPrefix1(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs)==0:
        return ''
    low = 0
    high = len(strs[0])
    while high>0:
        tmp = strs[0][low:high]
        if all(map(lambda x: tmp == x[low:high], strs)):#compare char segment between in [low,midlle+1)
            return tmp
        else:
            high-=1
    return ''
print('second')

print(longestCommonPrefix1(['a','aa','aaaa','aac']))
print(longestCommonPrefix1(['aaa','aa','aaaa','aac']))
print(longestCommonPrefix1(['ca','a']))
print(longestCommonPrefix1(["a","a","b"]))
print(longestCommonPrefix1(['aac','ab']))