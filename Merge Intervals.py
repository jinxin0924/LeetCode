__author__ = 'Xing'
# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        l=[]
        for inter in intervals:
            start,end=inter.start,inter.end
            l+=[[1,start],[2,end]]
        l_sorted=sorted(l,key=lambda d:(d[1],d[0]))
        result=[]
        stack=[]
        for p in l_sorted:
            if p[0]==1:
                stack.append(p[1])
            elif p[0]==2:
                if len(stack)==1:
                    result.append(Interval(stack.pop(),p[1]))
                else:
                    stack.pop()
        return result

s=Solution()
test=[[Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)],[Interval(1,4),Interval(4,5)]]
for p in test:
    result=s.merge(p)
    print([[i.start,i.end] for i in result])




