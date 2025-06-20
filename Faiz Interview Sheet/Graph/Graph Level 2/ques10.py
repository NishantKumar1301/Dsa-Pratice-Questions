#Question : Minimum Cost to Make at Least One Valid Path in a Grid
#Link to the question: https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/

from heapq import heappush,heappop

class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n,m = len(grid), len(grid[0])
        visited =[[False]*m for _ in range(n)]
        pq =[(0,0,0)]#cost,x,y
        dr,dc = [-1,0,1,0],[0,1,0,-1]
        dir_map ={4:0,1:1,3:2,2:3}
        while pq :
            cost,x,y = heappop(pq)
            if visited[x][y]:
                continue
            visited[x][y]=True
            if x==n-1 and y==m-1: #Indicates we have reached the destination
                return cost
            for i in range(4):
                nx,ny = x+dr[i],y+dc[i]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    ncost = cost
                    if i!= dir_map[grid[x][y]]:
                        ncost = cost+1
                    heappush(pq,(ncost,nx,ny))