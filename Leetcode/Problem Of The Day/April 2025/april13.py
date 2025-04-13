#Question : Count Good Numbers
#Link to the question: https://leetcode.com/problems/count-good-numbers/description/?envType=daily-question&envId=2025-04-13

MOD = 10**9+7
class Solution(object):
    def binary_exponential(self,a,b):
        res = 1
        while b>0:
            if b%2==1:
                res=(res*a)%MOD
            b = b//2
            a = (a*a)%MOD
        return res

    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        # odd= int(math.pow(4,n//2)) %MOD
        # even = int(math.pow(5,n-n//2)) % MOD
        # return (even *odd) %MOD
        odd = self.binary_exponential(4,n//2) % MOD
        even = self.binary_exponential(5,n-n//2)%MOD
        return (even*odd)%MOD


