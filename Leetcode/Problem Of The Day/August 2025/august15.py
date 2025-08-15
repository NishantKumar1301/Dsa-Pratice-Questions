#Question : Power of Four
#Link to the question: https://leetcode.com/problems/power-of-four/

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n ==0:
            return False
        while n%4==0:
            n = n //4
        if n ==1:
            return True
        else:
            return False