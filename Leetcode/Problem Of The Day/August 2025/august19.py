#Question : Number of Zero-Filled Subarrays
#Link to the question: https://leetcode.com/problems/number-of-zero-filled-subarrays/
class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, cnt = 0, 0
        for num in nums:
            if num == 0:
                cnt += 1
            else:
                cnt = 0
            ans += cnt
        return ans