#Question : Find the Maximum Length of Valid Subsequence I
#Link to the question: https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/
class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for pattern in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            cnt = 0
            for num in nums:
                if num % 2 == pattern[cnt % 2]:
                    cnt += 1
            res = max(res, cnt)
        return res
        