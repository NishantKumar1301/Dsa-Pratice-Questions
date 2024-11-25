#Question : Maximum Product Subarray
#Link to the question: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/maximum-product-subarray3604

def maxProduct(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    max_product = arr[0]
    current_max = arr[0]
    current_min = arr[0]
    
    for i in range(1, n):
        if arr[i] < 0:
            current_max, current_min = current_min, current_max
        
        current_max = max(arr[i], current_max * arr[i])
        current_min = min(arr[i], current_min * arr[i])
        
        max_product = max(max_product, current_max)
    
    return max_product