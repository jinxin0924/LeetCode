__author__ = 'Xing'
# The set [1,2,3,…,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
#1 "123"
#2 "132"
#3 "213"
#4 "231"
#5 "312"
#6 "321"
# Given n and k, return the kth permutation sequence.
import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        dict_n={0:1}
        for i in range(1,n):
            dict_n[i]=dict_n[i-1]*i
        result,number=[],[str(i) for i in range(1,n+1)]
        self.dfs(n,k,number,result,dict_n)
        return ''.join(result)
    def dfs(self,n,k,number,result,dict_n):
        if n==1:
            result.append(number[0])
            return
        index=(k-1)//dict_n[n-1]
        result.append(number[index])
        del number[index]
        self.dfs(n-1,min(k-index*dict_n[n-1],k),number,result,dict_n)

    def getPermutation2(self, n, k):
        res, now='', [i for i in range(1,n+1)]
        for i in range(n-1,-1,-1):
            index, k=(k-1)/math.factorial(i), k%math.factorial(i)
            res+=str(now[index])
            del now[index]
        return res
s=Solution()
print(s.getPermutation(1,1))