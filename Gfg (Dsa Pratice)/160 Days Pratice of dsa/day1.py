#Question : Second Largest
#Link to the question: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/second-largest3735

def getSecondLargest(self, arr):
        # Code Here
        max1=max2=-1
        n = len(arr)
        for i in range(n):
            if arr[i]>max1:
                max2 = max1
                max1 = arr[i]
            elif arr[i]>max2 and arr[i] !=max1:
                max2 = arr[i]
        return max2
