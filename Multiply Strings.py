__author__ = 'Xing'
# Given two numbers represented as strings, return multiplication of the numbers as a string.
#
# Note: The numbers can be arbitrarily large and are non-negative.
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result=''
        l1=len(num1)
        l2=len(num2)
        addition=0
        for step in range(2,l1+l2+2):
            total=0
            for i in range(1,l1+1):
                j=step-i
                if j<=0:break
                if j>l2:continue
                total+=int(num1[l1-i])*int(num2[l2-j])
            total+=addition
            result=str(total%10)+result
            addition=total//10
        index=0
        while result[index]=='0' and index<=l1+l2-2:index+=1
        return result[index:]
s=Solution()
print(s.multiply('123','325'))
print(s.multiply('9','9'))
print(s.multiply('0','0'))
print(s.multiply('9000','0'))
