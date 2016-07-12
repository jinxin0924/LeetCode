__author__ = 'Xing'
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer,
# replace the number by the sum of the squares of its digits,
#  and repeat the process until the number equals 1 (where it will stay),
#  or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        current=sum([int(i)**2 for i in str(n)])
        while (current!=1 and current!=4):
            current=sum([int(i)**2 for i in str(current)])
        return True if current==1 else False

s=Solution()
print(s.isHappy(19))
print(s.isHappy(3))
print(s.isHappy(6))
print(s.isHappy(1))
print(s.isHappy(82))