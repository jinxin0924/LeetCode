__author__ = 'Xin'
# Given a collection of distinct numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        self.dfs([],set(nums),result)
        return [list(i) for i in result]


    def dfs(self,ans,set1,result):
        if set1:
            for i in set1:
                self.dfs(ans+[i],set1-set([i]),result)
        else:
            result.append(ans)
    #考虑插入
    def permute2(self, nums):
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in xrange(len(perm)+1):
                    new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
            perms = new_perms
        return perms
s=Solution()
test=[[1,2,3],[1],[1,2]]
for case in test:
    print(s.permute(case))
