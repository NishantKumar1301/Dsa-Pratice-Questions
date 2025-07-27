#Question : Maximum Median Sum of Subsequences of Size 3
#Link to the question: https://leetcode.com/contest/weekly-contest-460/problems/maximum-median-sum-of-subsequences-of-size-3/
class Solution(object):
    def maximumMedianSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #[1,1,2,2,3,3]
        ans , n = 0 , len(nums)
        nums.sort()
        for i in range(n-2,n//3-1,-2):
            ans+=nums[i]
        return ans