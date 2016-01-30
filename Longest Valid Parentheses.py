__author__ = 'Xing'
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1={}
        stack,m=[],0
        for index in range(len(s)):
            letter=s[index]
            # print(letter,current,stack,m)
            if letter=='(':
                stack.append(index)
            elif letter==')':
                if stack:
                    start=stack.pop()
                    length=index+1-start
                    dict1[index],dict1[start]=length,length
                    m=max(m,length)
                    if start-1 in dict1:
                        dict1[index],dict1[start]=length+dict1[start-1],length+dict1[start-1]
                        m=max(m,length+dict1[start-1])
        return m


s=Solution()
# test=["","(()",")()())","()(()","()(())","((()))())","(()()","()()"]
test=["()()"]
for case in test:
    print(s.longestValidParentheses(case))
