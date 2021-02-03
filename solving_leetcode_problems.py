
#200. Number of Islands
"""An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water."""



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helperfunc(i,j,grid):
            if i>=0 and j>=0 and i<len(grid) and j<len(grid[i]) and grid[i][j]=="1":
                grid[i][j]="-1"
                helperfunc(i+1,j,grid)
                helperfunc(i-1,j,grid)
                helperfunc(i,j+1,grid)
                helperfunc(i,j-1,grid)
            
        
        num_of_island=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=='1':
                    num_of_island+=1
                    helperfunc(i,j ,grid)
        return num_of_island
        