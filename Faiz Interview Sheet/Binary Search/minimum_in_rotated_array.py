#Question : Find Minimum in Rotated Sorted Array
#Link to the question: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Minimum will be the first element of the sorted part
        n = len(nums)
        low,high = 0 ,n-1
        mini = float('inf')
        while low<=high:
            mid = low+(high-low)//2
            if nums[low]<=nums[mid]: #The left half is sorted
                mini = min(mini,nums[low])
                low = mid+1 #Now neglects the left as no more minimum will be in left
            else:
                mini = min(mini,nums[mid])
                high = mid-1 #neglects the right part
        return mini