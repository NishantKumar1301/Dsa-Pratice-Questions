#Question : Count Unguarded Cells in the Grid
#Link to the question : https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution(object):
    def dfs(self,row,col,grid,dir,freq):
        n = len(grid)
        m = len(grid[0])
        if row< 0 or col<0 or row>=n or col >= m :
            return 
        if (row,col) in freq:
            return
        grid[row][col] =1  #Mark the visited as 1
        if dir == "r":
            self.dfs(row,col+1,grid,"r",freq)
        if dir == "l":
            self.dfs(row,col-1,grid,"l",freq)
        if dir == "u":
            self.dfs(row-1,col,grid,"u",freq)
        if dir == "d":
            self.dfs(row+1,col,grid,"d",freq)
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[0]*n for _ in range(m)]
        freq={}
        for x,y in guards:
            freq[(x,y)]=1
            grid[x][y]=2 # Mark guard as 2
        for x , y in walls:
            freq[(x,y)]=1
            grid[x][y]=3 #Mark the wall as 3
        
        #Perform the dfs for the guard in all the 4 directtions
        for row,col in guards:
            self.dfs(row,col+1,grid,"r",freq)
            self.dfs(row,col-1,grid,"l",freq)
            self.dfs(row+1,col,grid,"d",freq)
            self.dfs(row-1,col,grid,"u",freq)
        
        #Return the number of unguided cell which have value == 0
        return sum (1 for i in range(m) for j in range(n) if grid[i][j]==0)
        