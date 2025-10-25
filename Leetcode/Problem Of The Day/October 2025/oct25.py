#Question : Calculate Money in Leetcode Bank
#Link to the question: https://leetcode.com/problems/calculate-money-in-leetcode-bank
class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        monday = 1
        while n > 0:
            for day in range(min(n, 7)):
                ans += monday + day
            n -= 7
            monday += 1
        return ans