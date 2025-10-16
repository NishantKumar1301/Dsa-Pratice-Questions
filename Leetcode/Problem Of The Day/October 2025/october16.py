#Question : Smallest Missing Non-negative Integer After Operations
#Link to the question: https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/
from collections import Counter


class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        mp = Counter(x % value for x in nums)
        mex = 0
        while mp[mex % value] > 0:
            mp[mex % value] -= 1
            mex += 1
        return mex