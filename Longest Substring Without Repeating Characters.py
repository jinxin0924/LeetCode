__author__ = 'JxKing'
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc",
# which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

def lengthOfLongestSubstring(s):  #dynamic programming,inspired by greatest sum of slice
    """
    :type s: str
    :rtype: int
    """
    lmax='' #record the longest substring
    current='' # new substring
    for word in s:
        if word not in current:
            current+=word
            if len(current)>len(lmax):
                lmax=current
        else:
            current=current[current.find(word)+1:]+word
    return len(lmax)
print(lengthOfLongestSubstring('abcabcbb'),3)
print(lengthOfLongestSubstring('bbbb'),1)
print(lengthOfLongestSubstring('b'),1)
print(lengthOfLongestSubstring(''),0)
print(lengthOfLongestSubstring('au'),2)
print(lengthOfLongestSubstring('aab'),2)