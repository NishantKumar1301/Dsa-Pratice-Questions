#Question : Maximum Path Sum in the matrix
#Link to the question: ttps://www.naukri.com/code360/problems/maximum-path-sum-in-the-matrix_797998

def getMaxPathSum(matrix):
    #   Write your code here
    n, m = len(matrix),len(matrix[0])
    dp = [[0]*m for _ in range(n)]
    for j in range(m):
        dp[0][j]=matrix[0][j]
    for i in range(1,n):
        for j in range(m):
            curr = matrix[i][j]
            up = curr + dp[i-1][j]
            left_diagonal ,right_diagonal = curr,curr
            if j-1>=0:
                left_diagonal+=dp[i-1][j-1]
            else:
                left_diagonal+=float('-inf')
            if j+1<m:
                right_diagonal+=dp[i-1][j+1]
            else:
                right_diagonal+=float('-inf')
            dp[i][j]=max(up,left_diagonal,right_diagonal)

    maxi = float('-inf')
    for j in range(m):
        ans = dp[n-1][j]
        maxi = max(maxi,ans)
    return maxi




























