#Question :  Shortest Path in Binary Matrix
#Link to the question: https://leetcode.com/problems/shortest-path-in-binary-matrix/

from heapq import heappush , heappop
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        visited =[[False]*n for _ in range(n)]
        dist = [[float('inf')]*n for _ in range(n)]
        dist[0][0]=1
        pq =[(1,0,0)]
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1 #The last as well as the first cell is non visited
        dr =[-1,-1,0,1,1,1,0,-1]
        dc = [0,1,1,1,0,-1,-1,-1]
        while pq:
            cost,x,y = heappop(pq)
            if visited[x][y]:
                continue
            visited[x][y]=True
            if x==n-1 and y==n-1:
                return cost
            for i in range(8):
                nx,ny = x+dr[i],y+dc[i]
                if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and grid[nx][ny]==0:
                    dist[nx][ny]=cost+1
                    heappush(pq,(dist[nx][ny],nx,ny))
        return -1