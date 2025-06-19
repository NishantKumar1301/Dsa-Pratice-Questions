#Question : Rotting Oranges
#Link to the question: https://leetcode.com/problems/rotting-oranges/

from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque()
        n,m = len(grid),len(grid[0])
        visited =[[0]*m for _ in range(n)]
        dr =[-1,0,1,0]
        dc = [0,1,0,-1]
        freshApple = 0
        ans =0
        fresh_apple_converted_to_rotten = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2: #Mark the visited as rotten and at t=0
                    queue.append((i,j,0))
                    visited[i][j]=2
                if grid[i][j]==1:
                    freshApple+=1 
        
        while queue:
            row,col,time = queue.popleft()
            ans = max(ans,time)
            for i in range(4):
                nrow,ncol = row+dr[i],col+dc[i]
                if 0<=nrow<n and 0<=ncol<m and visited[nrow][ncol]==0 and grid[nrow][ncol]==1:
                    queue.append((nrow,ncol,time+1)) # Append the neighbour row,col and time+1
                    visited[nrow][ncol]=2 # Since the fresh apple have been rotten so mark it as 2 
                    fresh_apple_converted_to_rotten+=1
        
        #If there is any fresh apple left so return -1
        if fresh_apple_converted_to_rotten != freshApple : #Means that still fresh apple is left
            return -1
        return ans

