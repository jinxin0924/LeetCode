__author__ = 'Xing'
# Given a non-negative number represented as an array of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        pre=1
        for index in range(len(digits)-1,-1,-1):
            s=pre+digits[index]
            digits[index]=s%10
            if s>=10:
                pre=1
            else:
                pre=0
                break
        if pre:
            digits.insert(0,1)
        return digits

s=Solution()
print(s.plusOne([9,9,9]))