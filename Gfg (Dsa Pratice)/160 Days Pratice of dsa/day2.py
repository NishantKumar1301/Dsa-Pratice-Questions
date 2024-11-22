#Question :Move All Zeroes to End
#Link to the question: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/move-all-zeroes-to-end-of-array0751

def pushZerosToEnd(self,arr):
    # code here
    n = len(arr)
    zero_index=0
    for i in range(n):
        if arr[i]!=0:
            arr[i],arr[zero_index] = arr[zero_index],arr[i]
            zero_index+=1
    return arr