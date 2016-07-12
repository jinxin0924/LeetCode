__author__ = 'Xing'
# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import random
        def topK(nums,k,ans):
            pivot=nums[random.randint(0,len(nums)-1)]
            left,right,middle=[],[],[]
            for number in nums:
                if number<pivot:
                    left.append(number)
                elif number>pivot:
                    right.append(number)
                else:
                    middle.append(number)
            if len(right)>k:
                return topK(right,k,ans)
            elif len(right)==k:
                return ans+right
            else:
                ans+=right
                if len(middle)>=k-len(right):
                    return ans+middle[:k-len(right)]
                else:
                    ans+=middle
                    return topK(left,k-len(right)-len(middle),ans)

        countDict={}
        for number in nums:
            if number not in countDict:
                countDict[number]=0
            countDict[number]+=1
        NBDict={}
        numList=[]
        for number in countDict:
            NBDict.setdefault(countDict[number],[]).append(number)
            if number not in numList:
                numList.append(countDict[number])
        ans=topK(numList,k,[])
        result=[]
        print(ans)
        for number in ans:
            result+=NBDict[number]
        return list(set(result))


s=Solution()
# print(s.topKFrequent([1,1,1,2,2,3],2))
print(s.topKFrequent([1,2],2))