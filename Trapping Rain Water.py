__author__ = 'Xing'
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
#
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<=2:return 0
        dict1={}
        first=self.Max2(height,dict1) #最大值
        second=dict1[first] #第二大的值
        index_list=[]
        total=0
        for i in range(len(height)): #记录第二高
            if height[i]==first:
                height[i]=second
                index_list.append(i)
            if height[i]==second:
                index_list.append(i)
        a,b=index_list[0],index_list[-1]
        for i in range(a,b):
            total+=second-height[i]
        return total+self.trap(height[:a+1])+self.trap(height[b:])
    def Max2(self,list1,dict1):
        if len(list1)==2:
            a,b=list1[0],list1[1]
            return self.compare(a,b,dict1)
        if len(list1)==1:return list1[0]
        mid=len(list1)//2
        left=self.Max2(list1[:mid],dict1)
        right=self.Max2(list1[mid:],dict1)
        return self.compare(left,right,dict1)

    def compare(self,a,b,dict1):
        if a>b:
            if a not in dict1:dict1[a]=b
            else:dict1[a]=max([b,dict1[a]])
            return a
        else:
            if b not in dict1:dict1[b]=a
            else:dict1[b]=max([a,dict1[b]])
            return b
# s=Solution()
# print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<=2:return 0
        index_end=len(height)-1
        while not height[index_end]:
            index_end-=1
        index_start=0
        while not height[index_start]:
            index_start+=1
        height=height[index_start:index_end+1]
        first,second=0,0
        index1,index2=0,0
        for index in range(len(height)):
            if height[index]>=first:
                first,second=height[index],first
                index1,index2=index,index1
            if first>height[index]>second:second,index2=height[index],index
        if index2<index1:index1,index2=index2,index1
        total=0
        print(index1,index2)
        for i in range(index1,index2):
            if height[i] <second:
                total+=second-height[i]
        return total+self.trap(height[:index1+1])+self.trap(height[index2:])
s=Solution()
# print(s.trap([8,5,4,1,8,9,3,0,0]))
# print(s.trap([4,2,3]))
# print(s.trap([9,3,0,0]))
# print(s.trap([3,0,0]))
# print(s.trap([2,0,2]))
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        n = len(height)
        l, r, water, minHeight = 0, n - 1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while r > l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water
s=Solution()
print(s.trap([8,5,4,1,8,9,3,0,0]))