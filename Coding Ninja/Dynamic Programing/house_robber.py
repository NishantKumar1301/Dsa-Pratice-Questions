#Question : House Robber II
#Link to the question: https://www.naukri.com/code360/problems/house-robber_839733

#Method 1 : Using Tablulation 

class Solution(object):
    def robLinear(self,nums):
            n = len(nums)
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return dp[n-1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If there is only one house, return its value
        if len(nums) == 1:
            return nums[0]
        
        # Case 1: Rob from house 0 to house n-2 (exclude last house)
        case1 = self.robLinear(nums[:-1])
        
        # Case 2: Rob from house 1 to house n-1 (exclude first house)
        case2 = self.robLinear(nums[1:])
        
        return max(case1, case2)


#Method2 : Using Memoization 

from os import *
from sys import *
from collections import *
from math import *

def helper(ind, arr, dp):
    if ind == 0:
        return arr[ind]
    if ind < 0:
        return 0
    
    if dp[ind] != -1:
        return dp[ind]
    
    take = helper(ind - 2, arr, dp) + arr[ind]
    not_take = helper(ind - 1, arr, dp)
    
    dp[ind] = max(take, not_take)
    return dp[ind]

def houseRobber(valueInHouse):
    n = len(valueInHouse)
    
    if n == 0:
        return 0
    if n == 1:
        return valueInHouse[0]
    
    # Case 1: Rob from house 0 to house n-2 (exclude last house)
    dp = [-1] * (n - 1)  
    case1 = helper(n - 2, valueInHouse[:n - 1], dp)  
    
    # Case 2: Rob from house 1 to house n-1 (exclude first house)
    dp = [-1] * (n - 1)  
    case2 = helper(n - 2, valueInHouse[1:], dp) 
    
    # Return the maximum of both cases
    return max(case1, case2)



