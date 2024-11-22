#Question : Rotate the array by k place
#Link to the question:  https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/rotate-array-by-n-elements-1587115621


class Solution:
    def reverse(self,left,right,arr):
        while(left<right):
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d = d%n
        self.reverse(0,d-1,arr)
        self.reverse(d,n-1,arr)
        self.reverse(0,n-1,arr)
        return arr