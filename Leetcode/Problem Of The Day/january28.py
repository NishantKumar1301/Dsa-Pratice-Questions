#Question : Maximum Number of Fish in a Grid
#Link to the question: https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/


class Solution(object):
    def is_valid(self,x,y,n,m):
        return 0<=x<n and 0<=y<m

    def dfs(self,grid,visited,x,y,n,m):
        dx =[0,0,1,-1]
        dy =[1,-1,0,0]
        ans = grid[x][y]
        for i in range(4):
            new_x = x+ dx[i]
            new_y = y+dy[i]
            if (self.is_valid(new_x,new_y,n,m)) and visited[new_x][new_y] and grid[new_x][new_y]!=0:
                visited[new_x][new_y]=True
                ans += self.dfs(grid,visited,new_x,new_y,n,m)
        return ans

    def findMaxFish(self, grid):
        n,m,ans = len(grid), len(grid[0]),0
        visited = [[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j]!=0:
                    visited[i][j]=True
                    ans = max(ans , self.dfs(grid,visited,i,j,n,m))
        return ans

