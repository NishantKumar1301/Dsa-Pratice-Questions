#Question : Minimal Cost
#Link to the question: https://www.geeksforgeeks.org/problems/minimal-cost/1

class Solution:
    #Method 1 : Using Tabulation
    def minimizeCost(self, k, arr):
        # code here
        n = len(arr)
        dp = [-1]*n
        dp[0]=0
        for i in range(1,n):
            minStep = float('inf')
            for j in range(1,k+1):
                if i-j>=0:
                    jump = dp[i-j]+abs(arr[i]-arr[i-j])
                    minStep= min(minStep,jump)
            dp[i]=minStep
        return dp[n-1]
    
    
    #Method 2 : Using Tabulation
    def minimizeCost(self, k, arr):
        #code here
        n = len(arr)
        dp = [-1]*n
        return self.helper(n-1,arr,dp,k)
    
    def helper(self,n,arr,dp,k):
        if n ==0:
            return 0
        if dp[n]!= -1:
            return dp[n]
        minStep = float('inf')
        for i in range(1,k+1):
            if n - i>=0:
                jump = self.helper(n-i,arr,dp,k)+abs(arr[n]-arr[n-i]) 
                minStep = min(minStep,jump)
        dp[n]=minStep
        return dp[n]
