__author__ = 'Xing'
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=set()
        index_set=set([i for i in range(len(nums))])
        self.dfs([],nums,result,index_set,set())
        return [list(i) for i in result]


    def dfs(self,ans,nums,result,index_set,set1):
        if len(set1)<len(nums):
            for i in index_set-set1:
                self.dfs(ans+[nums[i]],nums,result,index_set,set1|set([i]))
        else:
            result.add(tuple(ans))

    def permute2(self, nums):
        # perms = [[]]
        # for n in nums:
        #     new_perms = []
        #     for perm in perms:
        #         for i in range(len(perm)+1):
        #             new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
        #     perms = new_perms
        # return perms

        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break              #handles duplication
            ans = new_ans
        return ans
s=Solution()
# test=[[1,2,3],[1],[1,2],[1,1,2]]
test=[[3,3,0,0,2,3,2]]
for case in test:
    print(s.permute2(case))