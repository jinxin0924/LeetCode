__author__ = 'Xing'
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
#
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        left,right=[],[]
        list1=[[1,newInterval.start],[2,newInterval.end]]
        for p in intervals:
            if p.end<newInterval.start:
                left.append(p)
            elif newInterval.end<p.start:
                right.append(p)
            else:
                list1+=[[1,p.start],[2,p.end]]
        sorted_list=sorted(list1,key=lambda d:(d[1],d[0]))
        stack=[]
        mid=[]
        for p in sorted_list:
            if p[0]==1:
                stack.append(p[1])
            if p[0]==2:
                if len(stack)==1:
                    mid.append(Interval(stack.pop(),p[1]))
                else:
                    stack.pop()
        return left+mid+right

    def insert2(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left = [i for i in intervals if i.end < s]
        right = [i for i in intervals if i.start > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)].start)
            e = max(e, intervals[~len(right)].end)
        return left + [Interval(s, e)] + right


s=Solution()
# test=[[Interval(1,2),Interval(3,6),Interval(8,10),Interval(15,18)],[Interval(1,4),Interval(4,5)],[Interval(1,5)]]
test=[[Interval(1,5)]]
for p in test:
    result=s.insert(p,Interval(6,8))
    print([[i.start,i.end] for i in result])


