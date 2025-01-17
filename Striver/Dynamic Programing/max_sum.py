#Question : Maximum sum of non-adjacent elements
#Link to the question: https://www.naukri.com/code360/problems/maximum-sum-of-non-adjacent-elements_843261

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

#Method 1: using tabulation
def maximumNonAdjacentSum(nums):    
    # Write your code here.
    n = len(nums)
    dp = [-1]*n
    dp[0]=nums[0]
    for i in range(1,n):
        pick = nums[i]
        if i>1:
            pick+=dp[i-2]
        not_pick = 0+dp[i-1]
        dp[i]=max(pick,not_pick)
    return dp[n-1]

#Method 2: using Memoization
def helper(ind,arr,dp):
    if ind==0:
        return arr[ind]
    if ind<0:
        return 0
    if dp[ind]!=-1:
        return dp[ind]
    take = arr[ind]+helper(ind-2,arr,dp)
    not_take = 0+helper(ind-1,arr,dp)
    dp[ind]= max(take,not_take)
    return dp[ind]

def maximumNonAdjacentSum(nums):
    n = len(nums)
    dp=[-1]*n
    return helper(n-1,nums,dp) 
    

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1


