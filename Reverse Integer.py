__author__ = 'Xing'
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            s = str(0-x)
            s = s[::-1]
            x = 0-int(s)
        else:
            s = str(x)[::-1]
            x = int(s)
        if x > math.pow(2,31) or x < -math.pow(2,31):
            x = 0
        return x