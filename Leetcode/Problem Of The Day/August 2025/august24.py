#Question : Longest Subarray of 1's After Deleting One Element
#Link to the question: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeroCnt = 0
        maxLength = 0
        i = 0
        n = len(nums)
        for j in range(n):
            if nums[j]==0:
                zeroCnt+=1
            while zeroCnt>1:
                if nums[i]==0:
                    zeroCnt-=1
                i+=1
            maxLength = max(maxLength,j-i)
        return maxLength