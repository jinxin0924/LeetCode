__author__ = 'Xing'
# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combinations.

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        candidates.sort(reverse=True)
        list1=[]
        self.recursion(candidates,target,list1,result)
        return result

    def recursion(self,candidates,target,list1,result):
        if len(candidates)==0:return
        newcandidates=candidates.copy()
        current=newcandidates.pop()
        for count in range((target//current)+1):
            newtarget=target-count*current
            newlist1=list1.copy()
            for i in range(count):
                newlist1.append(current)
            if newtarget==0:
                result.append(newlist1)
                break
            self.recursion(newcandidates,newtarget,newlist1,result)

s=Solution()
print(s.combinationSum([1],2))

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        candidates.sort(reverse=True)
        self.dfs(candidates,target,[],result)
        return result
    def dfs(self,nums,target,path,result):
        if target<0:
            return
        if target==0:
            result.append(path)
        for i in nums:
            self.dfs(nums,target-i,path+[i],result)
s=Solution()
print(s.combinationSum([10,1,2,7,6,1,5],8))