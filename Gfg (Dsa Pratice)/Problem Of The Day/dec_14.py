#Question : Search in Rotated Sorted Array
#Link to the question: https://www.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1

class Solution:
    def search(self,arr,key):
        # Complete this function
        for ind , val in enumerate(arr):
            if val==key:
                return ind
        return -1


