#Question : Build Array from Permutation
#Link to the question: https://leetcode.com/problems/build-array-from-permutation/?envType=daily-question&envId=2025-05-06

class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        return [nums[nums[_]] for _ in range(n)]

