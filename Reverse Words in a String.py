__author__ = 'Xing'
# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList=s.split()
        sList.reverse()
        return ' '.join(sList)

s=Solution()
print(s.reverseWords("the sky is blue"))