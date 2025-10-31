#Question : The Two Sneaky Numbers of Digitville
#Link to the question: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville
class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
            if count[x] == 2:
                res.append(x)
        return res