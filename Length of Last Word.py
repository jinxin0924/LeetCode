__author__ = 'Xing'
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
#  return the length of last word in the string.
#
# If the last word does not exist, return 0.
class Solution(object):
    def lengthOfLastWord2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        return len(s.strip().split(' ')[-1])

    def lengthOfLastWord(self, s):
        i = len(s) - 1
        while i >= 0 and s[i] == ' ': i -= 1
        j = i - 1
        while j >= 0 and s[j] != ' ': j -= 1
        return 0 if i < 0 else i - j
s=Solution()
print(s.lengthOfLastWord("H"))