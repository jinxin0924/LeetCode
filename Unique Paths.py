__author__ = 'Xing'
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
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cache={}
        return self.recurs(m,n)
    @memo
    def recurs(self,m,n):
        if m==1 or n==1:
            return 1
        return self.recurs(m-1,n)+self.recurs(m,n-1)

import math

class Solution1(object):
    def c(self,n,r):
        f = math.factorial
        return int(f(n) / f(r) / f(n-r))
    def uniquePaths(self, m, n):
        return self.c(m+n-2,m-1)



s=Solution1()
s1=Solution()
print(s.uniquePaths(3,4))
print(s1.uniquePaths(3,4))
