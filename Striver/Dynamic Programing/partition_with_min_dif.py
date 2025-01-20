#Question : Array partition with minimum difference
#Link to the question: https://www.naukri.com/code360/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum._842494?leftPanelTabValue=PROBLEM

from typing import List

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    # write your code here
    total = sum(arr)
    dp=[[False]*(total+1) for _ in range(n)]
    for i in range(n):
        dp[i][0]=True
    if total>=arr[0]:
        dp[0][arr[0]]=True
    for ind in range(1,n):
        for target in range(1,total+1):
            not_take = dp[ind-1][target]
            take = False
            if target>=arr[ind]:
                take = dp[ind-1][target-arr[ind]]
            dp[ind][target]=take or not_take 
    mini = float('inf')
    for i in range(total+1):
        if dp[n-1][i]==True:
            s1 = i
            s2 = total-i  
            diff = abs(s2-s1)
            mini = min(mini,diff)
    return mini



