#Question : Frog Jump
#Link to the question: https://www.naukri.com/code360/problems/frog-jump_3621012

from os import *
from sys import *
from collections import *
from math import *

from typing import *

#Method1 : Using tabulation
def frogJump(n: int, heights: List[int]) -> int:
    # Write your code here.
    if n ==0:
        return 0
    dp = [-1]*(n)
    dp[0]=0
    for i in range(1,n):
        jump2 = float('inf')
        jump1 = dp[i-1]+abs(heights[i]-heights[i-1])
        if i > 1 : 
            jump2 = dp[i-2] +abs(heights[i]-heights[i-2])
        dp[i]=min(jump1,jump2)
    return dp[n-1]

#Method2 : Using Memoization
def helper(n, arr, dp):
    if n == 0:  
        return 0
    if dp[n] != -1:  
        return dp[n]
    
    jump1 = helper(n-1, arr, dp) + abs(arr[n] - arr[n-1])
    jump2 = float('inf')
    if n > 1:
        jump2 = helper(n-2, arr, dp) + abs(arr[n] - arr[n-2])
    
    dp[n] = min(jump1, jump2)
    return dp[n]

def frogJump(n: int, heights: List[int]) -> int:
    dp = [-1] * n
    return helper(n-1, heights, dp)






