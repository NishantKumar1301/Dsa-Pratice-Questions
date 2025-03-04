#Question : Check if Number is a Sum of Powers of Three
#Link to the question: https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/?envType=daily-question&envId=2025-03-04

class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :r type: bool
        """
        power = 0

        while 3**power <= n:
            power += 1

        while n > 0:
            if n >= 3**power:
                n -= 3**power
            if n >= 3**power:
                return False
            power -= 1

        return True
        

