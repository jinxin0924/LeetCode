__author__ = 'Xing'
# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
class Solution(object):
    def simplifyPath(self, path):
        result = []
        pathList = path.split('/')
        for content in pathList:
            if content:
                if content == '..':
                    try:
                        result.pop()
                    except:
                        result = []
                elif content != '.':
                    result.append(content)
        return '/'+'/'.join(result)

s=Solution()
print(s.simplifyPath("/a/./b/../../c/"))
print(s.simplifyPath("/../"))
print(s.simplifyPath("/home//foo/"))
print(s.simplifyPath("/"))