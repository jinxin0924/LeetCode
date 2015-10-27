__author__ = 'Xing'
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return []
        pattern=set()
        stack=['(']
        self.parenthesis(n-1,n,stack,'(',pattern)
        return list(pattern)

    def parenthesis(self,left,right,stack,string,pattern):
        if left==0 and right==0:pattern.add(string)
        if stack==[] and left>0:
            self.parenthesis(left-1,right,stack+['('],string+'(',pattern)
        elif len(stack)>0 and (left>0 or right>0):
            if left>0 and right>0:
                self.parenthesis(left-1,right,stack+['('],string+'(',pattern)
                self.parenthesis(left,right-1,stack[:-1],string+')',pattern)
            elif right>0 and left==0:
                self.parenthesis(left,right-1,stack[:-1],string+')',pattern)
s=Solution()
print(s.generateParenthesis(3))

def generateParenthesis(self, n):
    def generate(p, left, right, parens=[]):
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens += p,
        return parens
    return generate('', n, n)
s=Solution()
print(s.generateParenthesis(3))

