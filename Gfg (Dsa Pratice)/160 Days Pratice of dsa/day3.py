#Question : Reverse a array
#Link to the question: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/reverse-an-array

def reverseArray(self, arr):
        # code here
        left , right =0,len(arr)-1
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        # arr.reverse()
        return arr