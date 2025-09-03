#Question : Search in Rotated Sorted Array
#Link to the question: https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low,high = 0, n-1
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid]==target:
                return mid
            #Check which half is sorted 
            if nums[low]<=nums[mid]: #It indicates the left half is sorted
                if nums[low]<=target<=nums[mid]: #Eliminate right half
                    high = mid-1
                else:
                    low = mid+1
            else: #The right half is sorted
                if nums[mid]<=target<=nums[high]:
                    low = mid+1
                else:
                    high = mid -1
        return -1
