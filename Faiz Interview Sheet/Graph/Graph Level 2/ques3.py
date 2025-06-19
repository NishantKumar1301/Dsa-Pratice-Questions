#Question : Surrounded Regions
#Link to the question: https://leetcode.com/problems/surrounded-regions/
from collections import deque
class Solution(object):
    def solve(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n,m = len(grid),len(grid[0])
        visited=[[0]*m for _ in range(n)]
        queue = deque()
        dr,dc =[-1,0,1,0],[0,1,0,-1]
        for i in range(n):
            for j in range(m):
                if i==0 or i==n-1 or j==0 or j==m-1:
                    if grid[i][j]=="O":
                        visited[i][j]=1
                        queue.append((i,j))
        while queue:
            row,col = queue.popleft()
            for i in range(4):
                nr,nc = row+dr[i],col+dc[i]
                if 0<=nr<n and 0<=nc<m and visited[nr][nc]==0 and grid[nr][nc]=="O":
                    queue.append((nr,nc))
                    visited[nr][nc]=1
        
        for i in range(n):
            for j in range(m):
                if visited[i][j]==0 and grid[i][j]=="O":
                    grid[i][j]="X"
        
        return grid