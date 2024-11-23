#Question : Add One To Number
#Link to the question: https://www.naukri.com/code360/problem-of-the-day/easy

from os import *
from sys import *
from collections import *
from math import *

def addOneToNumber(arr):
    #   Write your code here
    n = len(arr)

    #Step1 : Remove the strting zeros from the input

    ind = 0
    while ind< n and arr[ind]==0:
        ind+=1
    
    arr = arr[ind:]

    #Step2 : If all the 0 have been removed then the array =[0]
    if not arr:
        arr=[0]

    n = len(arr)

    #Step 3 : 
    for i in range(n-1,-1,-1):
        if arr[i]<9:
            arr[i]+=1
            break
        arr[i]=0
    
    #Step 4 : If 999 then current == 000 then we need to append 1000

    if arr[0]==0:
        arr = [1]+arr

    return arr
