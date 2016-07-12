__author__ = 'Xing'
# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
# Given s = "hello", return "holle".
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        vowels=['a','e','i','o','u','A','E','I','O','U']
        stack=[]
        indexList=[]
        for index in range(len(s)):
            if s[index] in vowels:
                stack.append(s[index])
                indexList.append(index)
        for index in indexList:
            s[index]=stack.pop()
        return ''.join(s)

s=Solution()
# print(s.reverseVowels("hello"))
# print(s.reverseVowels("leetcode"))
print(s.reverseVowels("ai"))
print(s.reverseVowels("aA"))