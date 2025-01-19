#Question : Triangle
#Link to the question: https://www.naukri.com/code360/problems/triangle_1229398

#Method1 : Using Memoisation 

class Solution(object):
    def helper(self,i,j,arr,dp):
        if dp[i][j]!=-1:
            return dp[i][j]
        if i==len(arr)-1:
            return arr[i][j]
        down = arr[i][j]+self.helper(i+1,j,arr,dp)
        diagonal= arr[i][j]+self.helper(i+1,j+1,arr,dp)
        dp[i][j]=min(down , diagonal)
        return dp[i][j]

    def minimumTotal(self, triangle):
        m = len(triangle)
        #Grid length = m*m
        dp =[[-1]*m for _ in range(m)]
        return self.helper(0,0,triangle,dp)
    
#Method 2 : Using Tabulation 

from os import *
from sys import *
from collections import *
from math import *

def minimumPathSum(triangle, n):
    # Write your code here.
    dp=[[0]*n for _ in range(n)]
    #Base case : if i==n-1 return triangle[i][j], j=0,1,2 ,, n-1
    for i in range(n):
        dp[n-1][i]=triangle[n-1][i]

    for i in range(n-2,-1,-1):
        for j in range(i,-1,-1):
            down = triangle[i][j]+dp[i+1][j]
            diagonal = triangle[i][j]+dp[i+1][j+1]
            dp[i][j]=min(down,diagonal)
    return dp[0][0]



