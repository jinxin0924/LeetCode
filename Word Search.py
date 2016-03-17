__author__ = 'Xing'
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
#
# For example,
# Given board =
#
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

class Solution(object): #DFS
    def exist(self, board, word): #TLE
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n,m=len(board),len(board[0])
        # print(n,m)
        stack=[]
        for index1 in range(n):
            for index2 in range(m):
                if board[index1][index2]==word[0]:
                    visit=set()
                    visit.add(tuple([index1,index2]))
                    stack.append([[index1,index2],0,visit]) #record the current position, the word's length visited, and the position visited
        # print(stack)
        while stack:
            current=stack.pop()
            index1,index2,l,visited=current[0][0],current[0][1],current[1],current[2].copy()
            # print(index1,index2,l,visited,board[index1][index2])
            if l==len(word)-1:return True
            for p,q in [[index1,index2+1],[index1,index2-1],[index1+1,index2],[index1-1,index2]]:
                if p>=0 and q>=0 and p<n and q<m:
                    # print(p,q,board[p][q])
                    if board[p][q]==word[l+1]:
                        t=tuple([p,q])
                        if t not in visit:
                            visited.add(t)
                            stack.append([[p,q],l+1,visited])
        return False

    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res





s=Solution()
# print(s.exist([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ],'ABCCED'))
# print(s.exist([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ],'ABCB'))

# print(s.exist([['a', 'a']],'aaa'))
print(s.exist([list('abce'),list('sfes'),list('adee')],'abceseeefs'))