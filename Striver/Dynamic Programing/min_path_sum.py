#Question : Minimum Path Sum
#Link to the question:  https://www.naukri.com/code360/problems/minimum-path-sum_985349

#Method 1 : Using Memoisation 

class Solution(object):
    def helper(self,i,j,grid,dp):
        if i==0 and j==0:
            return grid[i][j]
        if i<0 or j<0:
            return float('inf')
        if dp[i][j]!=-1:
            return dp[i][j]
        up = grid[i][j]+self.helper(i-1,j,grid,dp)
        left = grid[i][j]+self.helper(i,j-1,grid,dp)
        dp[i][j]=min(up,left)
        return dp[i][j]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n ,m = len(grid),len(grid[0])
        dp = [[-1]*m for _ in range(n)]
        return self.helper(n-1,m-1,grid,dp)

        


