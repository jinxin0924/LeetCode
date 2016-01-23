__author__ = 'Xing'
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
#  return the length of last word in the string.
#
# If the last word does not exist, return 0.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        return len(s.strip().split(' ')[-1])
s=Solution()
print(s.lengthOfLastWord("H"))