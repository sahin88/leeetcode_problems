
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
        
#55 Jump Game 
#Solution 1

class Solution:
    can_jump=False
    def canJump(self, nums: List[int]) -> bool:
        pos=0
        destination=len(nums)-1
       
        def helperfunc(pos):
            if pos==destination:
                self.can_jump=True
                return True
        
            max_jump=nums[pos]
            for i in range(1,max_jump+1,1):
                if (helperfunc(pos+i)):
                    break


        helperfunc(pos)
            
        
        return self.can_jump
#169. Majority Element
#Solution 1

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        treshold=len(nums)/2 #1.5
        collections={}
        max_value=0
        max_key=0
        #{3:2,2:1}
        for item in nums:
            if item not in collections:
                collections[item]=1
            else:
                collections[item]+=1
        for key, values in collections.items():
            if values>treshold or values>max_value:
                #3,2
                max_value=values #2
                max_key=key #3
        return max_key

#132 Gas STation
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        index_of_station=len(gas) #5
        start_index=None
        for i in range(index_of_station):
            if gas[i]-cost[i]>=0:
                start_index=i
                actual_gas=0
                for j in range(index_of_station):
                    rel_index=j+start_index
                    if rel_index>index_of_station-1:
                            rel_index=rel_index-index_of_station
                    actual_gas=actual_gas+gas[rel_index]-cost[rel_index]

                    if actual_gas<0:
                        break
                    if j == index_of_station-1 and actual_gas>=0:
                        return start_index
                    
                    
        return -1
                        
            
