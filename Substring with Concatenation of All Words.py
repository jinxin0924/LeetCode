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
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """


s=Solution()
print(s.findSubstring("barfoothefoobarman",["foo", "bar"]))