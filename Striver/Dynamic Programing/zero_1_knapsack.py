#Question :  0 1 Knapsack
#Link to the question: https://www.naukri.com/code360/problems/0-1-knapsack_920542

#Method 1 : Using Memoisation 

from sys import setrecursionlimit
setrecursionlimit(10**6)

def helper(ind, W, weight, value, dp):
    if ind == 0:
        if W >= weight[0]:
            return value[0]
        else:
            return 0

    if dp[ind][W] != -1:
        return dp[ind][W]

    not_take = helper(ind - 1, W, weight, value, dp)

    take = float('-inf')
    if W >= weight[ind]:
        take = value[ind] + helper(ind - 1, W - weight[ind], weight, value, dp)

    dp[ind][W] = max(take, not_take)
    return dp[ind][W]

def knapsack(weight, value, n, maxWeight):
    dp = [[-1 for _ in range(maxWeight + 1)] for _ in range(n)]
    return helper(n - 1, maxWeight, weight, value, dp)


#Method2 : using Tabulation

from os import *
from sys import *
from collections import *
from math import *

def knapsack(weight, value, n, maxWeight):
    dp = [[0] * (maxWeight + 1) for _ in range(n)]
    
    for W in range(weight[0], maxWeight + 1):
        dp[0][W] = value[0]
    
    for ind in range(1, n): 
        for W in range(maxWeight + 1): 
            not_take = dp[ind - 1][W]
            
            take = float('-inf')
            if W >= weight[ind]:
                take = value[ind] + dp[ind - 1][W - weight[ind]]
            
            dp[ind][W] = max(take, not_take)
    
    return dp[n - 1][maxWeight]



