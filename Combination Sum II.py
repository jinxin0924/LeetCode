__author__ = 'Xin'
# Given a collection of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combinations.
#

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        new_candidates=[i for i in candidates if i<target]
        new_candidates.sort(reverse=True)
        result=[]
        self.dfs(new_candidates,target,[],result)
        return result
    def dfs(self,nums,target,path,result):
        if target==0:
            if path not in result:
                result.append(path)
        if target<0:
            return
        if len(nums)==0:return
        newnums=nums[:]
        current=newnums.pop()
        self.dfs(newnums,target-current,path+[current],result)
        self.dfs(newnums,target,path,result)
s=Solution()
t=s.combinationSum2([23,32,22,19,29,15,11,26,28,20,34,5,34,7,28,33,30,30,16,33,8,15,28,26,17,10,25,12,6,17,30,16,6,10,23,22,20,29,14,5,6,5,5,6,29,20,34,24,16,7,22,11,17,7,33,21,13,15,29,6,19,16,10,21,21,28,8,6],27)
print(len(t))

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates.sort()
        combinations, stack = [], [(0, 0, [])]
        while stack:
            (total, start, combination) = stack.pop()
            for index in range(start, len(candidates)):
                sum = total + candidates[index]
                if sum < target:
                    if (index == start) or (candidates[index] != candidates[index-1]):
                        # avoid duplicates
                        stack.append((sum, index+1, combination + [candidates[index]]))
                else:
                    if sum == target:
                        combinations.append(combination + [candidates[index]])
                    # no need to try any more
                    break
        return combinations
s=Solution()
t=s.combinationSum2([23,32,22,19,29,15,11,26,28,20,34,5,34,7,28,33,30,30,16,33,8,15,28,26,17,10,25,12,6,17,30,16,6,10,23,22,20,29,14,5,6,5,5,6,29,20,34,24,16,7,22,11,17,7,33,21,13,15,29,6,19,16,10,21,21,28,8,6],27)
print(len(t))