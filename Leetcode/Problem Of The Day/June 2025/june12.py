#Question : Maximum Difference Between Adjacent Elements in a Circular Array
#Link to the question: https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/
class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = abs(nums[0]-nums[-1])
        n = len(nums)
        for i in range(n-1):
            maxi = max(abs(nums[i+1]-nums[i]),maxi)
        return maxi