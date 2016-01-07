__author__ = 'JxKing'
# Divide two integers without using multiplication, division and mod operator.
#
# If it is overflow, return MAX_INT.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==0:return 'MAX_INT'
        posivitive = (dividend < 0) is (divisor < 0)
        dividend,divisor=abs(dividend),abs(divisor)
        if dividend<divisor:return 0
        l1=len(str(divisor))
        dividend=str(dividend)
        l2=len(dividend)
        cur=dividend[:l1]
        result=''
        if int(cur)>=divisor:
            result,cur=self.d(int(cur),divisor)
        for index in range(l1,l2):
            cur=cur+dividend[index]
            t=self.d(int(cur),divisor)
            result+=t[0]
            cur=t[1]
        result=int(result)
        if not posivitive:result=-result
        return min(max(-2147483648, result), 2147483647)

    def d(self,a,b):
        t=0
        di=b
        b=0
        while b+di<=a:
                t+=1
                b+=di
        return str(t),str(a-b)

s=Solution()
print(s.divide(1,2))
print(s.divide(214,2))
print(s.divide(-21474836472,2))



