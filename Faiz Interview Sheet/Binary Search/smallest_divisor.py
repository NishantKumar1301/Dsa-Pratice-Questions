#Question : Find the Smallest Divisor Given a Threshold
#Link to the question: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
from math import ceil
class Solution(object):
    def check_threshold(self,arr,num,threshold):
        n = len(arr)
        total =0
        for i in range(n):
            total+=ceil(arr[i]/float(num))
        if total<=threshold:
            return True
        else:
            return False


    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        n = len(nums)
        low= 1
        high = max(nums) 
        # for i in range(mini,maxi+1):
        #     if self.check_threshold(nums,i,threshold):
        #         return i
        # return -1
        while low<=high:
            mid = (low+high)//2
            if self.check_threshold(nums,mid,threshold):
                high = mid -1
            else:
                low = mid + 1
        return low
