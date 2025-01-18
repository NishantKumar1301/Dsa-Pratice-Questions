#Question : Unique Paths
#Link to the question: https://www.naukri.com/code360/problems/unique-paths_1081470

#Method 1 : Using memoisation 

class Solution(object):
    def helper(self,i,j,dp):
        if dp[i][j]!=-1:
            return dp[i][j]
        if i==0 and j==0:
            return 1 
        if i<0 or j<0:
            return 0
        up = self.helper(i-1,j,dp)
        left = self.helper(i,j-1,dp)
        dp[i][j]=up+left
        return dp[i][j]
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #Size of dp = m*n 
        dp =[[-1 for j in range(n)]for i in range(m)]
        return self.helper(m-1,n-1,dp)
        
        
#


