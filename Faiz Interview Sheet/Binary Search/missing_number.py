#Question : Kth Missing Positive Number
#Link to the question: https://leetcode.com/problems/kth-missing-positive-number/
class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        low =0
        high = n-1
        while low<=high:
            mid = low + (high-low)//2
            missing = arr[mid]-(mid+1)
            if missing<k:
                low = mid+1
            else:
                high = mid -1
        return k+low