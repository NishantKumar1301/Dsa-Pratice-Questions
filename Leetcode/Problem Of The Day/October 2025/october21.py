#Question : Maximum Frequency of an Element After Performing Operations I
#Link to the question: https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/
from collections import Counter
from bisect import bisect_left,bisect_right
class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        nums.sort()
        maxFreq = 0
        counter = Counter(nums)
        for i in range(nums[0], nums[-1] + 1):
            left = bisect_left(nums, i - k)
            right = bisect_right(nums, i + k) - 1
            maxFreq = max(maxFreq, min(right - left + 1, counter[i] + numOperations))
        return maxFreq
        