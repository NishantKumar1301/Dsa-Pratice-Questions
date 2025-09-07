#Question : Split Array Largest Sum
#Link to the question: https://leetcode.com/problems/split-array-largest-sum/
class Solution(object):
    def calculate_number_of_ways_to_split(self,arr,limit):
        total =0
        ways =1
        n = len(arr)
        for i in range(n):
            if total + arr[i]<=limit:
                total+=arr[i]
            else:
                ways+=1
                total = arr[i]
        return ways

    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)<k:
            return -1
        low = max(nums)
        high = sum(nums)
        while low<=high:
            mid = low+(high-low)//2
            ways = self.calculate_number_of_ways_to_split(nums,mid)
            if ways>k:
                low= mid+1
            else:
                high = mid-1
        return low