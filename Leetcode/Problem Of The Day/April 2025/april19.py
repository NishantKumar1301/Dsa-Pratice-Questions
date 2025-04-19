#Question : Count the Number of Fair Pairs
#Link to the question: https://leetcode.com/problems/count-the-number-of-fair-pairs/description/?envType=daily-question&envId=2025-04-19

from bisect import bisect_left,bisect_right
class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(n-1):
            lb = bisect_left(nums,lower-nums[i],i+1)
            ub = bisect_right(nums,upper-nums[i],i+1)
            ans +=(ub-lb)
        return ans