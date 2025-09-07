#Question : Allocate Minimum Pages
#Link to the question: https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
class Solution:
    def countStudent(self,arr,limit):
        stud = 1
        total = 0
        n = len(arr)
        for i in range(n):
            if total+arr[i]<=limit:
                total+=arr[i]
            else:
                stud+=1
                total = arr[i]
        return stud

    def findPages(self, arr, k):
        # code here
        if len(arr)<k:
            return -1
        low = max(arr)
        high = sum(arr)
        while low<=high:
            mid = low+(high-low)//2
            no_of_stud = self.countStudent(arr,mid)
            if no_of_stud>k:
                low = mid+1
            else:
                high = mid -1
        return low