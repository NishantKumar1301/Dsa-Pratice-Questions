#Question : New 21 Game
#Link to the question: https://leetcode.com/problems/new-21-game/
class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        if k == 0:
            return 1.0
        windowSum = 0.0
        for i in range(k, k + maxPts):
            windowSum += 1 if i <= n else 0
        dp = {}
        for i in range(k - 1, -1, -1):
            dp[i] = windowSum / maxPts
            remove = 0.0
            if i + maxPts <= n:
                remove = dp.get(i + maxPts, 1.0)
            windowSum += dp[i] - remove
        return dp[0]