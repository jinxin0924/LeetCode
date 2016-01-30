__author__ = 'Xing'
# You are given a string, s, and a list of words, words,
# that are all of the same length.
# Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening characters.
#
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
#
# You should return the indices: [0,9].


class Solution(object):
    def findSubstring2(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:return []
        k=len(words[0])
        comb,index,num=[],0,len(words)
        result=[]
        words=sorted(words)
        while index+k<=len(s):
            word=s[index:index+k]
            if word in words:
                comb.append(word)
                index2=index+k
                while index2<index+k*num:
                    word=s[index2:index2+k]
                    if word in words:
                        comb.append(word)
                        index2+=k
                    else:
                        break
                if sorted(comb)==words:
                    result.append(index)
                index+=1
                comb=[]

            else:
                index+=1
        return result

    def findSubstring(self, s, words):
        if not s or not words:return []
        k,num=len(words[0]),len(words)
        words=sorted(words)
        list1=[]
        for j in range(k):
            list1.append([i for i in range(j,len(s)-k+1,k)])
        result=[]
        for p in list1:
            current=[]
            if len(p)<num:continue
            list2=[s[index:index+k] for index in p]
            for index in range(len(p)+1-num):
                if sorted(list2[index:index+num])==words:
                    result.append(p[index])
        return result

s=Solution()
print(s.findSubstring("barfoothefoobarman",["foo", "bar"]))
print(s.findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))
print(s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))
print(s.findSubstring("a",["a"]))
print(s.findSubstring("aaaaaaaa",["aa","aa","aa"]),s.findSubstring2("aaaaaaaa",["aa","aa","aa"]))





