__author__ = 'Xing'
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        if s=='':
            return True
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            elif i in [')',']','}']:
                if stack:
                    p=stack.pop()
                    if p+i not in ['()','[]','{}']:
                        return False
                else:return False
        return (stack==[])

sol= Solution()
print(sol.isValid('{'))
print(sol.isValid('{}'))
print(sol.isValid('}'))