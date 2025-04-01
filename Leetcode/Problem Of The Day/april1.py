#Question : Solving Questions With Brainpower
#Link to the question: https://leetcode.com/problems/solving-questions-with-brainpower/description/?envType=daily-question&envId=2025-04-01

class Solution(object):
    def solve(self,i,n,grid,dp):
        if i>=n:
            return 0
        if dp[i]!=-1:
            return dp[i]
        not_take = self.solve(i+1,n,grid,dp)
        take = self.solve(i+grid[i][1]+1,n,grid,dp)+grid[i][0]
        dp[i]= max(take,not_take)
        return dp[i]

    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :r type: int
        """
        n = len (questions)
        dp = [-1]*n
        return self.solve(0,n,questions,dp)
