#Question : Capacity To Ship Packages Within D Days
#Link to the question: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution(object):
    def calculate_number_of_days_to_load(self,arr,capacity):
        load =0
        days = 1
        n = len(arr)
        for i in range(n):
            if load+arr[i]>capacity:
                days+=1
                load = arr[i]
            else:
                load += arr[i]
        return days

    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        #Range of load will be from max element of arr to total sum of all the element of the array
        low = max(weights)
        high = sum(weights)
        while low<=high:
            mid = low+(high-low)//2
            if self.calculate_number_of_days_to_load(weights,mid)<=days:
                high = mid-1
            else:
                low = mid+1
        return low