#Question : Longest Nice Subarray
#Link to the question: https://leetcode.com/problems/longest-nice-subarray/description/?envType=daily-question&envId=2025-03-18


class Solution:
    def longestNiceSubarray(self, nums):
        used = 0  
        start = 0  
        ans = 0 
        for window_end in range(len(nums)):
            while used & nums[window_end] != 0:
                used ^= nums[
                    start
                ]  
                start += 1 

            used |= nums[window_end]

            ans = max(ans, window_end - start + 1)

        return ans