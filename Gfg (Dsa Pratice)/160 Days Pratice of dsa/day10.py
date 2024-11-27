#Question :Kadane's Algorithm
#Link to the question: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/kadanes-algorithm-1587115620

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        max_sum=float("-inf")
        right=curr_sum =0
        n = len(arr)
        while(right<n):
            curr_sum+=arr[right]
            
            max_sum = max(max_sum,curr_sum)

            if curr_sum<0:
                curr_sum =0
            
            # max_sum = max(max_sum,curr_sum)
            
            right+=1
        return max_sum

