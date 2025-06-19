#Question : Number of Islands
#Link to the question: https://leetcode.com/problems/number-of-islands/
class Solution(object):
    def dfs(self,row,col,grid,visited):
        n,m = len(grid),len(grid[0])
        visited[row][col]=True
        deltarow =[-1,0,1,0]
        deltacol = [0,1,0,-1]
        for i in range(4):
            nrow = row + deltarow[i]
            ncol = col+ deltacol[i]
            if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]=="1" and not visited[nrow][ncol]:
                self.dfs(nrow,ncol,grid,visited)
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n,m = len(grid),len(grid[0])
        ans =0
        visited = [[False]*m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                if not visited[row][col] and grid[row][col]=="1":
                    self.dfs(row,col,grid,visited)
                    ans +=1
        return ans
        