__author__ = 'Xing'
# Find all possible combinations of k numbers that add up to a number n,
#  given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        combination=[]
        for number in range(1,10):
            self.dfs([number],combination,k-1,n-number,number)
        return combination

    def dfs(self,current,combination,k,n,start):
        if k==0:
            if n==0:
                combination.append(current)
            return
        if n<=0:
            return
        for number in range(start+1,min(10,n+1)):
            self.dfs(current+[number],combination,k-1,n-number,number)

s=Solution()
print(s.combinationSum3(3,7))
print(s.combinationSum3(3,9))

