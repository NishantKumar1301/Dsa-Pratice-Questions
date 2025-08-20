#Question : Count Square Submatrices with All Ones
#Link to the question: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m,n = len(matrix),len(matrix[0])
        dp =[[-1]*n for _ in range(m)]
        #the first row and col value of dp should be same as the matrix
        for i in range(m):
            dp[i][0]=matrix[i][0]
        for i in range(n):
            dp[0][i]= matrix[0][i]
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    dp[i][j]=0
                else:
                    dp[i][j]= 1+ min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])

        ans = 0 
        for i in range(m):
            for j in range(n):
                ans+=dp[i][j]
        return ans
        