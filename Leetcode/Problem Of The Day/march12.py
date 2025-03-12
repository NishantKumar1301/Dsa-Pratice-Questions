#Question : Maximum Count of Positive Integer and Negative Integer
#Link to the question: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/?envType=daily-question&envId=2025-03-12

class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :r type: int
        """
        pos = sum(1 for num in nums if num>0)
        neg = sum(1 for num in nums if num<0)
        return max(pos,neg)
        

