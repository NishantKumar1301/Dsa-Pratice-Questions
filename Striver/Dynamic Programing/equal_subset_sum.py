#Question : Partition Equal Subset Sum
#Link to the question: https://www.naukri.com/code360/problems/partition-equal-subset-sum-_892980?leftPanelTabValue=PROBLEM

#Method1 :Using Memoisation 

class Solution(object):
    def helper(self,ind,target,arr,dp):
        if target==0:
            return True
        if ind==0:
            return arr[0]==target
        if dp[ind][target]!=-1:
            return dp[ind][target]
        take = False
        not_take = self.helper(ind-1,target,arr,dp)
        if target>=arr[ind]:
            take = self.helper(ind-1,target-arr[ind],arr,dp)
        dp[ind][target]= take or not_take
        return dp[ind][target]

    def canPartition(self, nums):
        n = len(nums)
        total = sum(nums)
        if total%2==1:
            return False
        else:
            target = total//2
            dp=[[-1]*(target+1) for _ in range(n)]
            return self.helper(n-1,target,nums,dp)
        
#Method2 : Using Tabulation

def canPartition(arr, n):
    # Write your code here.
    total = sum(arr)
    if total %2==1:
        return False
    else:
        target = total //2
        dp=[[False]*(target+1) for _ in range(n)]
        for i in range(n):
            dp[i][0]=True 
        if target>=arr[0]:
            dp[0][arr[0]]=True 
        for ind in range(1,n):
            for tar in range(1,target+1):
                not_take = dp[ind-1][tar]
                take = False
                if tar>=arr[ind]:
                    take = dp[ind-1][tar-arr[ind]]
                dp[ind][tar]=take or not_take 
        return dp[n-1][target]


