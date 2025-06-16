#Question : Count Sub Islands
#Link to the question: https://leetcode.com/problems/count-sub-islands/
class Solution(object):
    def dfs(self,row,col,grid1,grid2,visited):
        n,m = len(grid2),len(grid2[0])
        #Subisland = current in grid2 is land and it should be land in grid1 too
        is_sub_island = grid1[row][col]==1
        visited[row][col]=True
        dr =[-1,0,1,0]
        dc = [0,1,0,-1]
        for i in range(4):
            nrow,ncol = row+dr[i],col+dc[i]
            if (0<=nrow<n) and  (0<=ncol<m) and not visited[nrow][ncol] and grid2[nrow][ncol]==1:
                if not self.dfs(nrow,ncol,grid1,grid2,visited):
                    is_sub_island = False
        return is_sub_island
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        n , m = len(grid1),len(grid1[0])
        visited =[[False]*m for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid2[i][j]==1:
                    if self.dfs(i,j,grid1,grid2,visited) ==True:
                        ans+=1
        return ans