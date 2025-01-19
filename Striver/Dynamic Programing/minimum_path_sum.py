#Question :  Minimum Falling Path Sum
#Link to the question: https://leetcode.com/problems/minimum-falling-path-sum/description/

#Method 1 : Using memoisation

class Solution(object):
    def helper(self,i,j,col,arr,dp):
        if j<0 or j>=col:
            return float('inf')
        if i==0:
            return arr[0][j]
        if dp[i][j]!=-1:
            return dp[i][j]
        up = arr[i][j]+self.helper(i-1,j,col,arr,dp)
        left_diagonal = arr[i][j]+self.helper(i-1,j-1,col,arr,dp)
        right_diagonal = arr[i][j]+self.helper(i-1,j+1,col,arr,dp)
        dp[i][j]=min(up,left_diagonal,right_diagonal)
        return dp[i][j]

    def minFallingPathSum(self, matrix):
        n = len(matrix)
        dp =[[-1]*n for _ in range(n)]
        mini = float('inf')
        for j in range(n):
            ans = self.helper(n-1,j,n,matrix,dp)
            mini = min(mini,ans)
        return mini

#Method 2 : Using Tabulation
class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        dp = [[0]*n for _ in range(n)]
        #Base case : if i =0 , j =0,1,2,3,,,,,n
        for j in range(n):
            dp[0][j]=matrix[0][j]
        for i in range(1,n):
            for j in range(n):
                up = matrix[i][j]+dp[i-1][j]
                left_diagonal = matrix[i][j]
                if j-1>=0:
                    left_diagonal+=dp[i-1][j-1]
                else:
                    left_diagonal+=float('inf')
                right_diagonal = matrix[i][j]
                if j+1<n:
                    right_diagonal+=dp[i-1][j+1]
                else:
                    right_diagonal+=float('inf')
                dp[i][j]=min(up,left_diagonal,right_diagonal)
                
        mini = float('inf')
        for j in range(n):
            ans = dp[n-1][j]
            mini = min(ans,mini)
        return mini

