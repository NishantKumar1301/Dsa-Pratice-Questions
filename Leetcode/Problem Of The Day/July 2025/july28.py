#Question : Count Number of Maximum Bitwise-OR Subsets
#Link to the question: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
class Solution(object):
    def helper(self,idx,currOr,maxOr,nums,dp):
        if idx==len(nums):
            if currOr == maxOr:
                dp[idx][currOr]=1
                return dp[idx][currOr]
            dp[idx][currOr] = 0
            return 0
        if dp[idx][currOr]!=-1:
            return  dp[idx][currOr]
        take = self.helper(idx+1,currOr|nums[idx],maxOr,nums,dp)
        not_take = self.helper(idx+1,currOr,maxOr,nums,dp)
        dp[idx][currOr]=take+not_take
        return dp[idx][currOr]

    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxOr = 0
        for num in nums:
            maxOr= maxOr| num
        dp = [[-1]*(maxOr+1) for _ in range(n+1)]
        currOr = 0
        return self.helper(0,currOr,maxOr,nums,dp)
        