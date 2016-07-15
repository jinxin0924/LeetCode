# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
class Solution(object):


    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        def add2ans(current,ans):
            if len(current)>=2:
                ans.append(current[0]+'->'+current[-1])
            else:
                ans.append(current[0])
        ans=[]
        current=[]
        for index,number in enumerate(nums):
            if index==0:
                current=[str(number)]
                last=number
                continue
            if number==last+1:
                current.append(str(number))
            else:
                add2ans(current,ans)
                current=[str(number)]
            last=number
        if current:
            add2ans(current,ans)
        return ans

    def summaryRanges2(self, nums):
        ranges, r = [], []
        for n in nums:
            if n-1 not in r:
                r = []
                ranges += r,
            r[1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]

s=Solution()
print(s.summaryRanges([0,1,2,4,5,7]))
print(s.summaryRanges([0,1,2]))