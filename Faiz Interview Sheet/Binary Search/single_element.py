#Question : Single Element in a Sorted Array
#Link to the question: https://leetcode.com/problems/single-element-in-a-sorted-array/
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        If element is on the right half (even , odd)-> Eliminate left
        If element is on the left half (odd , even)-> Eliminate right
        """
        n = len(nums)
        if n==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]
        low = 1
        high = n-2 #We have covered base cases for 0 & n-1th index separately
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if ((mid %2==1 and nums[mid]==nums[mid-1]) or (mid %2==0 and nums[mid]==nums[mid+1])):
                low = mid+1
            else:
                high = mid-1
        return -1