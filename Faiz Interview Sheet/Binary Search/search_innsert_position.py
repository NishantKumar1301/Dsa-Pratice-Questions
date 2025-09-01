#Question : Search Insert Position
#Link to the question: https://leetcode.com/problems/search-insert-position/
from bisect import bisect_left
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = bisect_left(nums,target)
        return ans