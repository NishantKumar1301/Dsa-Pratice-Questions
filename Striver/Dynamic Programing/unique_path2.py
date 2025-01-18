#Question : Unique Paths II
#Link to the question: https://www.naukri.com/code360/problems/unique-paths-ii_977241

#Method 1 : Using Memoisation

class Solution(object):
    def helper(self,i,j,grid,dp):
        if i>=0 and j>=0 and grid[i][j]==1:
            return 0
        if i==0 and j ==0:
            return 1
        if i<0 or j<0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        up = self.helper(i-1,j,grid,dp)
        left = self.helper(i,j-1,grid,dp)
        dp[i][j]=up+left
        return dp[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp =[[-1]*n for _ in range(m)]
        return self.helper(m-1,n-1,obstacleGrid,dp)


