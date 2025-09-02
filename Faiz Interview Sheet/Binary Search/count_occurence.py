#Question : Number of occurrence
#Link to the question: https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1
from bisect import bisect_left , bisect_right
class Solution:
    def countFreq(self, arr, target):
        # code here
        n = len(arr)
        lb = bisect_left(arr, target)
        ub = bisect_right(arr, target)
        if lb ==n or arr[lb]!=target:
            return 0
        return ub-lb