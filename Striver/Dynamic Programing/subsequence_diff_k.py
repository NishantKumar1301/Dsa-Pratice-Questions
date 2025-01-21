#Question :  Partitions With Given Difference
#Link to the question: https://www.naukri.com/code360/problems/partitions-with-given-difference_3751628?leftPanelTabValue=PROBLEM

from typing import List  
    
class Solution:
    
    def helper(self,idx,target,arr,dp):
        if idx==0:
            if target==0 and arr[0]==0:
                return 2
            if target==0 or target==arr[0]:
                return 1
            return 0
        if dp[idx][target]!=-1:
            return dp[idx][target]
        not_take = self.helper(idx-1,target,arr,dp)
        take =0
        if arr[idx]<=target:
            take = self.helper(idx-1,target-arr[idx],arr,dp)
        dp[idx][target]=take+not_take 
        return dp[idx][target]
    
    
    def countPartitions(self, arr, d):
        # code here
        n = len(arr)
        total = sum(arr)
        if total-d<0 or (total-d)%2==1:
            return 0 
        target = (total-d)//2
        dp=[[-1]*(target+1) for _ in range(n)]
        return self.helper(n-1,target,arr,dp)
        


