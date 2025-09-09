#Question : Number of People Aware of a Secret
#Link to the question: https://leetcode.com/problems/number-of-people-aware-of-a-secret
MOD = 10**9+7
class Solution(object):
    def solve(self,day,delay,forget,dp):
        if day==1:
            return 1
        if dp[day]!=-1:
            return dp[day]
        ans =0
        for i in range(day-forget+1,day-delay+1):
            if i>0:
                ans=(ans+self.solve(i,delay,forget,dp))%MOD
        dp[day]=ans
        return dp[day]
        
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        ans = 0
        dp = [-1]*(n+1)
        for i in range(n-forget+1,n+1):
            ans = (ans+self.solve(i,delay,forget,dp))%MOD
        return ans
