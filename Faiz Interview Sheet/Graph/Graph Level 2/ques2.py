#Question : Number of Enclaves
#Link to the question: https://leetcode.com/problems/number-of-enclaves/

from collections import deque
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n,m,ans = len(grid),len(grid[0]) ,0
        queue = deque()
        dr,dc = [-1,0,1,0],[0,1,0,-1]
        visited=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                #Mark all the boundary 1s as visited
                if i==0 or i == n-1 or j==0 or j==m-1:
                    if grid[i][j]==1:
                        queue.append((i,j))
                        visited[i][j]=1
        while queue:
            row,col = queue.popleft()
            for i in range(4):
                nr,nc = row+dr[i],col+dc[i]
                if 0<=nr<n and 0<=nc<m and visited[nr][nc]==0 and grid[nr][nc]==1:
                    queue.append((nr,nc))
                    visited[nr][nc]=1
        
        #Ans = Count of all unvisited 1s
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and visited[i][j]==0:
                    ans += 1
        
        return ans