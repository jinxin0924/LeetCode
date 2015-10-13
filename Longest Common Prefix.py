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