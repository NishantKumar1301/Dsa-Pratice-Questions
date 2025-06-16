#Question : Maximum Difference Between Increasing Elements
#Link to the question:https://leetcode.com/problems/maximum-difference-between-increasing-elements/
class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1
        mini = nums[0]
        for i in range(len(nums)):
            if mini<nums[i]:
                ans = max(ans,nums[i]-mini)
            else:
                mini = nums[i]
        return ans
        