__author__ = 'Xing'
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:return '1'
        pre=self.countAndSay(n-1)
        result,index,count,length='',0,0,len(pre)
        while index<length:
            count+=1
            if index+1<length and pre[index]==pre[index+1]:
                index+=1
            else:
                result+=str(count)+pre[index]
                count=0
                index+=1
        return result

s=Solution()
# print(s.countAndSay(1))
for n in range(5):
    print(s.countAndSay(n))