#Question : Next Permutation
#Link to the question: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/next-permutation5226

def nextPermutation(self, arr):
        # code here
        n = len(arr)
        pivot = -1
        #Step1 : Find the pivot element
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                pivot = i
                break
        
        #Step2 : If pivot =-1 Simply it means it is the last permutation
        if pivot == -1:
            return arr.reverse()
        
        #Step3 : Swap the arr[pivot] with the just largest value than the arr[pivot]
        
        for i in range(n-1,pivot,-1):
            if arr[i]>arr[pivot]:
                arr[i],arr[pivot]=arr[pivot],arr[i]
                break
        
        #Step4 : Swap all the rest element from the right of pivot
        
        left,right = pivot+1,n-1
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
            
        return arr
