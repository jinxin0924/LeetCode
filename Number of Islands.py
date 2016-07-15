__author__ = 'Xing'
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans=0
        visited=set()
        for row,string in enumerate(grid):
            for col,letter in enumerate(string):
                if tuple([row,col]) in visited:
                    continue
                if letter=='1':
                    ans+=1
                    stack=[tuple([row,col])]
                    while stack:
                        point_row,point_col=stack.pop()
                        visited.add(tuple([point_row,point_col]))
                        if point_col>0:
                            point=tuple([point_row,point_col-1])
                            if point not in visited:
                                visited.add(point)
                                if grid[point_row][point_col-1]=='1':
                                    stack.append(tuple([point_row,point_col-1]))
                        if point_col<=len(string)-2:
                            point=tuple([point_row,point_col+1])
                            if point not in visited:
                                visited.add(tuple([point_row,point_col+1]))
                                if grid[point_row][point_col+1]=='1':
                                    stack.append(tuple([point_row,point_col+1]))
                        if point_row<=len(grid)-2 :
                            point=tuple([point_row+1,point_col])
                            if point not in visited:
                                visited.add(tuple([point_row+1,point_col]))
                                if grid[point_row+1][point_col]=='1':
                                    stack.append(tuple([point_row+1,point_col]))
                        if point_row>0:
                            point=tuple([point_row-1,point_col])
                            if point not in visited:
                                visited.add(tuple([point_row-1,point_col]))
                                if grid[point_row-1][point_col]=='1':
                                    stack.append(tuple([point_row-1,point_col]))
        return ans
s=Solution()
print(s.numIslands(["11110","11010","11000","00000"]))

print(s.numIslands(["11000","11000","00100","00011"]))
