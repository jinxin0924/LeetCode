__author__ = 'Xing'
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# For example:
#
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 0
        ans=num%9
        return 9 if ans==0 else ans

s=Solution()
print(s.addDigits(38))
print(s.addDigits(46))
print(s.addDigits(9))


