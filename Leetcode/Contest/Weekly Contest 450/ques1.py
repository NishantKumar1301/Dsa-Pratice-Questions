#Question : Smallest Index With Digit Sum Equal to Index
#Link to the question: https://leetcode.com/contest/weekly-contest-450/problems/smallest-index-with-digit-sum-equal-to-index/description/

class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            req = sum(int(d) for d in str(num))
            if req == i:
                return i
        return -1
