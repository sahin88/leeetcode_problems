
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
                   
# Java Solution  1725. Number Of Rectangles That Can Form The Largest Square
class Solution {
    public int countGoodRectangles(int[][] rectangles) {
        Map<Integer,Integer> hashmap= new HashMap<Integer,Integer>();
        
        for (int [] rectangle:rectangles){
            int min_val=Math.min(rectangle[0],rectangle[1]);
            
            int count=hashmap.containsKey(min_val)?hashmap.get(min_val):0;
            hashmap.put(min_val,count+1);
            
        }
        List<Integer> hasharr = new ArrayList<Integer>(hashmap.keySet());
        
         return hashmap.get(Collections.max(hasharr));
    }
}     
   

#1742. Maximum Number of Balls in a Box
##Python 
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        empty_dict={}
        for i in range( lowLimit, highLimit+1,+1):
            starter=0
            for j in str(i):
                starter+=int(j)
            if starter not in empty_dict:
                empty_dict[starter]=1
            else:
                empty_dict[starter]+=1
        return max(empty_dict.values())

## Java 
class Solution {
    public int countBalls(int lowLimit, int highLimit) {
        Map<Integer,Integer> hashmap= new HashMap<>();
        
        for(int i=lowLimit; i<highLimit+1; i++){
            int sum_digits=sum_of_digit(i);
            int counter=hashmap.containsKey(sum_digits)?hashmap.get(sum_digits):0;
            hashmap.put(sum_digits,counter+1);
                
        }
        
        return Collections.max(hashmap.values());
    }
    public int sum_of_digit(int nums){
        int sum=0;
        while(nums>0){
            sum= sum+nums % 10;
            nums=nums/10;
            
        }
        return sum;
    }
}
                

         
