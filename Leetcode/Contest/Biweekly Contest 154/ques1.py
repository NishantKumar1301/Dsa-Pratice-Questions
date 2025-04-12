#Question : Minimum Operations to Make Array Sum Divisible by K
#Link to the question: https://leetcode.com/contest/biweekly-contest-154/problems/minimum-operations-to-make-array-sum-divisible-by-k/?slug=minimum-operations-to-make-array-sum-divisible-by-k&region=global_v2

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :r type: int
        """
        sum_ = sum(nums)
        return sum_%k

