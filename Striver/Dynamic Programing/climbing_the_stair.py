#Question :  Count Ways To Reach The N-th Stair
#Link to the question: https://www.naukri.com/code360/problems/count-ways-to-reach-nth-stairs_798650

from os import *
from sys import *
from collections import *
from math import *

#Method 1 : Using Recursion : Gives Tle
def countDistinctWays(nStairs: int) -> int:
    #  Write your code here.
    if nStairs ==0 or nStairs ==1 :
        return 1 
    left = countDistinctWays(nStairs-1)
    right = countDistinctWays(nStairs-2)
    return left+right

#Method 2 : Using Tabulation : Bottom Up , SO much space complexity
def countDistinctWays(nStairs: int) -> int:
    if nStairs==0 or nStairs==1:
        return 1
    dp = [0]*(nStairs+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,nStairs+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[nStairs]

#Method 3 : Using Memoization  : Top Down Approach,More space complexity
def countDistinctWays(nStairs: int,memo={}) -> int:
    if nStairs==0 or nStairs==1:
        return 1
    if nStairs in memo:
        return memo[nStairs]
    left = countDistinctWays(nStairs-1,memo)
    right = countDistinctWays(nStairs-2,memo)
    memo[nStairs]= left+right
    return memo[nStairs]

#Method 4 : Iterative Way
def countDistinctWays(nStairs: int) -> int:
    if nStairs == 0:
        return 1
    elif nStairs == 1:
        return 1
    prev1 =prev2 =1
    for i in range(2,nStairs+1):
        curr = prev1+prev2
        prev2 = prev1
        prev1 = curr
    return prev1




