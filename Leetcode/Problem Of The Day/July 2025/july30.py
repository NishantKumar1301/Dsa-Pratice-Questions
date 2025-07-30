#Question : Longest Subarray With Maximum Bitwise AND
#Link to the question: https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=ans=streak =0
        for num in nums:
            if num>maxi:
                maxi = num
                streak = 0
                ans = 0
            if num==maxi:
                streak+=1
            else:
                streak = 0
            ans = max(ans,streak)
        return ans