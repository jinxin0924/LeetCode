__author__ = 'Xing'
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
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
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false
from functools import wraps
def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

class Solution(object):
    # For a 2d table, dp[i][j] would mean whether sub-pattern p[:i + 1]
    # matches sub-string s[:j + 1]. Most tricky part is
    # when the current pattern letter is *, suppose its index is i,
    #  p[:i + 1] will match sub-string s[:j + 1] if p[:i + 1] matches s[:j] or p[:i] matches s[:j + 1],
    # namely current cell value is true if its top or its left is true.
    #  Since the current row only depends on the previous row,
    # we can use two rolling lists to do the dp instead of a matrix.
    def isMatch2(self, s, p):
        l = len(s)
        if len(p) - p.count('*') > l:
            return False
        dp = [True] + [False] * l
        for letter in p:
            new_dp = [dp[0] and letter == '*']
            # print('new_dp',new_dp)
            if letter == '*':
                for j in range(l):
                    new_dp.append(new_dp[-1] or dp[j + 1])
            elif letter == '?':
                new_dp += dp[:l]
            else:
                new_dp += [dp[j] and s[j] == letter for j in range(l)]
            dp = new_dp
        return dp[-1]

    def isMatch(self,s,p):
        ls,lp=len(s),len(p)
        if s==p:return True
        if ls==0:return p=='*'
        if lp==0:return s=='*'
        return self.judge(len(s)-1,len(p)-1,s,p)
    @memo
    def judge(self,i,j,s,p):
        # print(i,j)
        if i==0 and j==0:
            return True
        if i<0 and j>=0:
            if p[:j+1]=='*'*(j+1):return True
            else:return False
        if i>=0 and j<0:
            if s[:i+1]=='*'*(i+1):return True
            else:return False
        if i<0 and j<0:
            return False
        # if i==1 and j==1:
        #     if s[i]==s[j]:return True
        m=[s[i],p[j]]
        # print(m)
        if '*' in m:
            return self.judge(i-1,j,s,p)|self.judge(i,j-1,s,p)
        if '?' in m:
            return self.judge(i-1,j-1,s,p)
        # print(i,j)
        # print(p[j])
        if s[i]==p[j]:
            return self.judge(i-1,j-1,s,p)
        return False

    def isMatch3(self,s,p): #错误的那步记录下来，错了就回头
        s_pointer,p_pointer,s_last,p_last,ls,lp=0,0,-1,-1,len(s),len(p)
        while s_pointer<ls:
            # print(s_pointer,p_pointer)
            if p_pointer<lp and (s[s_pointer]==p[p_pointer]):
                s_pointer+=1
                p_pointer+=1
            elif p_pointer<lp and p[p_pointer]=='?':
                s_pointer+=1
                p_pointer+=1
            elif p_pointer<lp and p[p_pointer]=='*':
                p_pointer+=1
                s_last,p_last=s_pointer,p_pointer
            elif p_last!=-1:
                s_last+=1
                s_pointer,p_pointer=s_last,p_last
            else:
                return False
        while p_pointer<lp and p[p_pointer]=='*':
            p_pointer+=1
        return (p_pointer==lp) and (s_pointer==ls)




s = Solution()
test=[["abefcdgiescdfimde","ab*cd?i*de"],["abefcdgiescdfimde","ab*cd?i*fimde"],['aa','a'],['aa','aa'],['aa','*'],['c','*?*'],["abbabbbaabaaabbbbbabbabbabbbabbaaabbbababbabaaabbab","*aabb***aa**a******aa*"]]
# test=[["aa","a"]]
for words in test:
    # print(s.isMatch(words[0],words[1]),s.isMatch2(words[0],words[1]))
    print(s.isMatch3(words[0],words[1]),s.isMatch2(words[0],words[1]))
