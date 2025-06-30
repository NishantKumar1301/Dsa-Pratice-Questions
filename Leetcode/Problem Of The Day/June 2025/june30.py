#Question : Longest Harmonious Subsequence
#Link to the question:  https://leetcode.com/problems/longest-harmonious-subsequence/

from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        ans =0
        for num in nums:
            mini= num
            maxi = num+1
            if maxi in freq:
                ans = max(ans,freq[maxi]+freq[mini])
        return ans
