#Question : Minimum Operations to Make Array Values Equal to K
#Link to the question: https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/?envType=daily-question&envId=2025-04-09

class Solution(object):
    def minOperations(self, nums, k):
        s = set()
        for num in  nums:
            if num<k:
                return -1
            elif num>k:
                s.add(num)
        return len(s)

