#Question : Number of Closed Islands
#Link to the question: https://leetcode.com/problems/number-of-closed-islands/
class Solution(object):
    def dfs(self,grid,row,col,visited):
        n,m = len(grid),len(grid[0])
        if row<0 or row>=n or col <0 or col>=m:
            return False
        if visited[row][col] or grid[row][col]==1:
            return True
        visited[row][col]=True
        left = self.dfs(grid,row-1,col,visited)
        right = self.dfs(grid,row+1,col,visited)
        up = self.dfs(grid,row,col-1,visited)
        down = self.dfs(grid,row,col+1,visited)
        return left and right and up and down

    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n,m = len(grid),len(grid[0])
        ans = 0
        visited = [[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0 and not visited[i][j]:
                    if self.dfs(grid,i,j,visited):
                        ans+=1
        return ans