__author__ = 'Xing'
# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la,lb=len(a),len(b)
        if la<lb:
            la,lb=lb,la
            a,b=b,a
        result=''
        pre=0
        for index in range(lb-1,-1,-1):
            s=int(a[index])+int(b[index])+pre
            if s==0 or s==1:
                pre=0
                result=str(s)+result
            if s==2 or s==3:
                pre=1
                result=str(s%2)+result
        return a[:(la-lb)]+result

s=Solution()
print(s.addBinary('111','1'))
print(s.addBinary('110','1'))
