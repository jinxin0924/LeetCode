__author__ = 'Xing'
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        capitals={chr(x): index+1 for index,x in enumerate(range(ord('A'), ord('Z')+1))}
        result=0
        index=0
        for letter in s[::-1]:
            result+=capitals[letter]*(26**index)
            index+=1
        return result

s=Solution()
print(s.titleToNumber('A'))
print(s.titleToNumber('AA'))