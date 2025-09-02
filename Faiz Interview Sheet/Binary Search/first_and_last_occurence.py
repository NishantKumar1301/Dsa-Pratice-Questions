#Question : Find First and Last Position of Element in Sorted Array
#Link to the question: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from bisect import bisect_left , bisect_right
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        lower_bound = bisect_left(nums,target)
        upper_bound = bisect_right(nums,target)
        """
        If the lower bounds returns n , which is the length of nums, then it means target is not present
        if nums[lower_bound]!= target then it also means that target is not present in nums so return [-1,-1]
        else return [lower_bound,upper_bound-1], as upperbound-1 will give the last occurence
        """
        if lower_bound==n or nums[lower_bound]!=target:
            return [-1,-1]
        return [lower_bound, upper_bound-1]