#Question :  Subset Sum Equal To K
#Link to the question: https://www.naukri.com/code360/problems/subset-sum-equal-to-k_1550954?leftPanelTabValue=PROBLEM

#Method 1 : Using memoisation
class Solution:
    def helper(self,ind,target,arr,dp):
        if target==0:
            return True
        if ind==0:
            return arr[ind]==target
        if dp[ind][target]!=-1:
            return dp[ind][target]
        not_take = self.helper(ind-1,target,arr,dp)
        take = False
        if target>=arr[ind]:
            take = self.helper(ind-1,target-arr[ind],arr,dp)
        dp[ind][target]=take or not_take
        return dp[ind][target]
            
    def isSubsetSum (self, arr, target):
        # code here 
        n = len(arr)
        dp=[[-1]*(target+1) for _ in range(n)]
        return self.helper(n-1,target,arr,dp)
    
#Method2 : Using Tabulation

def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    dp=[[False]*(k+1) for _ in range(n)]
    for i in range(n):
        dp[i][0]=True
    if arr[0]<=k:
        dp[0][arr[0]]=True  
    for ind in range(1,n):
        for target in range(k+1):
            not_take = dp[ind-1][target]
            take = False
            if target>=arr[ind]:
                take = dp[ind-1][target-arr[ind]]
            dp[ind][target]=take or not_take
    return dp[n-1][k]
    


