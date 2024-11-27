#Question : Smallest Positive Missing Number
#Link to the question: https://www.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        arr.sort()
        target =1
        for i in range(0,len(arr)):
            if arr[i]==target and arr[i]>0:
                target+=1
        return target



