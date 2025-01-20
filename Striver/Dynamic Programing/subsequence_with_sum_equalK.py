#Question : Count Subsets with Sum K
#Link to the question: https://www.naukri.com/code360/problems/count-subsets-with-sum-k_3952532

#Method 1 :Using memoisation

class Solution:
    def helper(self,idx,target,arr,dp):
        if idx==0:
            if target==0 and arr[idx]==0:
                return 2
            if target ==0 or target == arr[0]:
                return 1
            return 0
        if dp[idx][target]!=-1:
            return dp[idx][target]
        not_take = self.helper(idx-1,target,arr,dp)
        take =0
        if target>=arr[idx]:
            take = self.helper(idx-1,target-arr[idx],arr,dp)
        dp[idx][target]=take+not_take
        return dp[idx][target]

def perfectSum(self, arr, target):
		# code here
		n = len(arr)
		dp=[[-1]*(target+1) for _ in range(n)]
		return self.helper(n-1,target,arr,dp)

#Method 2 : Using Tabulation

from typing import List
MOD = 10**9+7
def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    n = len(arr)
    arr.sort(reverse=True)
    dp=[[0]*(k+1) for _ in range(n)]
    for i in range(n):
        dp[i][0]=1 
    if k>=arr[0]:
        dp[0][arr[0]]=1 
    for idx in range(1,n):
        for target in range(1,k+1):
            not_take = (dp[idx-1][target]) %MOD
            take = 0
            if target>=arr[idx]:
                take = (dp[idx-1][target-arr[idx]])%MOD
            dp[idx][target]=(take+not_take )%MOD
    return dp[n-1][k]





