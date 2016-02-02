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
        for index in range(1,la+1):
            if index<=lb:
                s=int(a[-index])+int(b[-index])+pre
                if s==0 or s==1:
                    pre=0
                    result=str(s)+result
                if s==2 or s==3:
                    pre=1
                    result=str(s%2)+result
            else:
                s=int(a[-index])+pre
                if s==0 or s==1:
                    return a[:(-index)]+str(s)+result
                elif s==2:
                    pre=1
                    result='0'+result
            if index==la:
                if pre==0:return result
                return str(pre)+result

        # print(result)


s=Solution()
print(s.addBinary('111','1'))
print(s.addBinary('110','1'))
print(s.addBinary('1101','1'))
print(s.addBinary('1','1'))
print(s.addBinary('0','1'))

