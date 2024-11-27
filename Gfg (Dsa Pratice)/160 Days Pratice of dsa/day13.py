#Question : Max Circular Subarray Sum
#Link to the question: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/max-circular-subarray-sum-1587115620

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    
    #Finding the maximum subarray sum
    def kadane_max_sum(nums):
        curr_sum =0
        max_sum = float("-inf")
        for n in nums:
            curr_sum+=n
            max_sum=max(curr_sum,max_sum)
            if curr_sum<0:
                curr_sum=0
        return max_sum
    
    #Finding the minimum subarray sum
    def kadane_min_sum(nums):
        curr_sum =0
        min_sum=float("inf")
        for n in nums:
            curr_sum+=n
            min_sum=min(min_sum,curr_sum)
            if curr_sum>0:
                curr_sum=0
        return min_sum
    
    min_sum = kadane_min_sum(arr)
    max_sum = kadane_max_sum(arr)

    #Step1 : Find the total sum
    total_sum = sum(arr)
    
    #Step 2: Find the circular sum = total-min_sum
    circular_sum = total_sum - min_sum
    
    #Step 3: if all the element of the array is negative then we should return the maximum sum of the negative values of the array
    #Because the max_sum will return the maximum value of the sum
    
    if max_sum<0:
        return max_sum
    
    #Step4 : else we should return the max of circular_sum and the max_sum
    return max(max_sum,circular_sum)
    
    
