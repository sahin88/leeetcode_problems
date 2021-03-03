
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
                
#####206. Reverse Linked List
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        while head:
            temp=head
            head=head.next
            temp.next=prev
            prev=temp
        return prev
            
####700. Search in a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        self.result=None
        def helperfunc(root):
            if root is None:
                return
            if root and root.val==val:
                self.result=root
            helperfunc(root.right)
            helperfunc(root.left)
            
            
        helperfunc(root)
        return self.result
            

### 98 Validate Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helperfunc(root):
            if not root:
                return True
            if root.val>root.val:
                return False
            if root.right.val<root.val:
                return False   
        
            return helperfunc(root.left) and helperfunc(root.right)
        return helperfunc(root)

##142. Linked List Cycle 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow =head, head
        while fast and fast.next:
            slow, fast=slow.next, fast.next.next
            if slow== fast:
                break
        else:
            return 
        pointer=head
        
        while pointer!=slow:
            pointer=pointer.next
            slow=slow.next
        return pointer
### 141 LInked List Cycle 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow=head, head
       
        
        while fast and fast.next:
            print(fast.next.next.val,fast.next.val)
            fast, slow= fast.next.next, slow.next
            
            if fast==slow:
                return True
        return False
        

### 547 Number of Proviences

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited_city={}
        proviences=0
        for i in range(len(isConnected)):
            if i not in visited_city:
                visited_city[i]=False
        
        def helperfunc(city, city_connections):  
            visited_city[city]=True
            for cities ,item  in enumerate(city_connections): 
                if item==1 and  not visited_city[cities] :
                    helperfunc(cities,isConnected[cities])
        for city, city_connections in enumerate(isConnected):
            if  not visited_city[city]:
                proviences+=1
                helperfunc(city,city_connections)
            
        
        return proviences
            

         
