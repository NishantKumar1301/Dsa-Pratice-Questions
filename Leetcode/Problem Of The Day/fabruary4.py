#Question : Maximum Ascending Subarray Sum
#Link to the question: https://leetcode.com/problems/maximum-ascending-subarray-sum/description/?envType=daily-question&envId=2025-02-04

class Solution(object):
    def maxAscendingSum(self, nums):
        n,curr_sum,ans = len(nums),nums[0],0
        for i in range(1,n):
            if nums[i]<=nums[i-1]:
                ans = max(curr_sum,ans)
                curr_sum =0
            curr_sum +=nums[i]
        ans = max(ans,curr_sum)
        return ans        

