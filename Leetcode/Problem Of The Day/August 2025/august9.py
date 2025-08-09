#Question : Power of Two
#Link to the question: https://leetcode.com/problems/power-of-two/
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & (n - 1))