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
        less,more=intervals[0],intervals[0]
        result=[]
        for p in intervals:
            if p.start<newInterval.start and p.start>less.start:
                result.append(less)
                less=p
            elif p.start>newInterval.start and p.start<less.start:
                result.append(more)
                more=p
            else:result.append(p)
        if less.end