#Question : Maximum Points
#Link to the question: https://www.naukri.com/code360/problem-of-the-day/easy


from os import *
from sys import *
from collections import *
from math import *

from typing import *

def maximumPoints(n: int, grid: List[List[int]]) -> int:
    # Write your code here.
    primary_diagonal_sum = secondary_daigonal_sum =0
    
    for i in range(n):
        primary_diagonal_sum+=grid[i][i]
        secondary_daigonal_sum +=grid[i][n-1-i]
    
    #If n = odd then remove the center element as it have been found twice which is at arr[n//2][n//2]
    
    if n%2 ==1 :
        return secondary_daigonal_sum+primary_diagonal_sum-grid[n//2][n//2]
    
    return secondary_daigonal_sum+primary_diagonal_sum


