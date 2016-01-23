__author__ = 'Xing'
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls,lp=len(s),len(p)
        s_pointer,p_pointer,last_s,last_p=ls-1,lp-1,-1,-1
        while s_pointer>=0 :
            if p_pointer>=0 and p[p_pointer]=='*':
                last_s,last_p=s_pointer,p_pointer
                p_pointer-=1
            elif  p_pointer>=0 and p[p_pointer]=='.':
                p_pointer-=1
                s_pointer-=1
            elif p_pointer>=0 and s[s_pointer]==p[p_pointer]:
                p_pointer-=1
                s_pointer-=1
            elif last_p!=-1:
                s_pointer=last_s-1
                p_pointer=last_p
            else:return False
        if p[p_pointer]=='*':p_pointer=-1
        return p_pointer==-1 and s_pointer==-1

s=Solution()
test=[("aa","a"),("aa","aa"),("aaa","aa"),("aa","a*"),("aa", ".*"),("ab", ".*"),("aab", "c*a*b")]
# test=[('aa','aa')]
for p in test:
    print(s.isMatch(p[0],p[1]))