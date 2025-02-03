#Question : Longest Strictly Increasing or Strictly Decreasing Subarray
#Link to the question: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/?envType=daily-question&envId=2025-02-03

class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :r type: int
        """
        ans = 0
        for start in range(len(nums)):
            curr_length = 1
            for pos in range(start + 1, len(nums)):
                if nums[pos] > nums[pos - 1]:
                    curr_length += 1
                else:
                    break
            ans = max(ans, curr_length)

        for start in range(len(nums)):
            curr_length = 1
            for pos in range(start + 1, len(nums)):
                if nums[pos] < nums[pos - 1]:
                    curr_length += 1
                else:
                    break
            ans = max(ans, curr_length)

        return ans  
        

