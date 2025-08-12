#Question : Ways to Express an Integer as Sum of Powers
#Link to the question: https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

MOD = 10**9+7
class Solution(object):
    def solve(self,n,num,x,dp):
        if n==0:
            return 1
        if n<0:
            return 0
        power = pow(num,x)
        if power>n:
            return 0
        if dp[n][num]!=-1:
            return dp[n][num]
        take = self.solve(n-power,num+1,x,dp)
        not_take = self.solve(n,num+1,x,dp)
        dp[n][num]= (take+not_take) % MOD
        return dp[n][num]

    def numberOfWays(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        dp = [[-1]*301 for _ in range(301)]
        return self.solve(n,1,x,dp)