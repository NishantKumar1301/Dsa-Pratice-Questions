#Question : Partition Equal Subset Sum
#Link to the question: https://leetcode.com/problems/partition-equal-subset-sum/description/?envType=daily-question&envId=2025-04-07

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
        