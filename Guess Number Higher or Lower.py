__author__ = 'Xing'
# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I'll tell you whether the number is higher or lower.
#
# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
#
# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
target=6

def guess(num):
    global target
    if num<target:
        return -1
    if num==target:
        return 0
    if num>target:
        return 1

class Solution(object):
    def guessNumber(self, n,s=1):
        """
        :type n: int
        :rtype: int
        """
        mid=(n+s)//2
        if guess(mid)==1:
           return self.guessNumber(mid,1)
        if guess(mid)==0:
            return mid
        if guess(mid)==-1:
            return self.guessNumber(n,mid)

s=Solution()
print(s.guessNumber(10))