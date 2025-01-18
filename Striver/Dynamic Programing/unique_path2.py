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
    
#Method2 : Using Tabulation

MOD = 10**9 + 7
def mazeObstacles(n, m, mat):
    # Write your code here.
    dp =[[-1]*m for _ in range(n)]
    dp[0][0]=1
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                continue
            if i>=0 and j>= 0 and mat[i][j]==-1:
                dp[i][j]=0
                continue
            up,left=0,0
            if i>0: 
                up=dp[i-1][j] % MOD
            if j>0:
                left=dp[i][j-1] % MOD
            dp[i][j]=(left+up)%MOD
    return dp[n-1][m-1]


