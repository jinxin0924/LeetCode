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

class Solution(object):
    # For a 2d table, dp[i][j] would mean whether sub-pattern p[:i + 1]
    # matches sub-string s[:j + 1]. Most tricky part is
    # when the current pattern letter is *, suppose its index is i,
    #  p[:i + 1] will match sub-string s[:j + 1] if p[:i + 1] matches s[:j] or p[:i] matches s[:j + 1],
    # namely current cell value is true if its top or its left is true.
    #  Since the current row only depends on the previous row,
    # we can use two rolling lists to do the dp instead of a matrix.
    def isMatch(self, s, p):
        l = len(s)
        if len(p) - p.count('*') > l:
            return False
        dp = [True] + [False] * l
        for letter in p:
            new_dp = [dp[0] and letter == '*']
            if letter == '*':
                for j in range(l):
                    new_dp.append(new_dp[-1] or dp[j + 1])
            elif letter == '?':
                new_dp += dp[:l]
            else:
                new_dp += [dp[j] and s[j] == letter for j in range(l)]
            dp = new_dp
        return dp[-1]


s = Solution()
print(s.isMatch('aa', 'a'))
print(s.isMatch("aa", "aa"))
print(s.isMatch("aab", "*a*bc"))


