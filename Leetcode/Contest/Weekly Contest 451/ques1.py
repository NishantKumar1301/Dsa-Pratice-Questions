#Question : Find Minimum Log Transportation Cost
#Link to the question: https://leetcode.com/contest/weekly-contest-451/problems/find-minimum-log-transportation-cost/

class Solution(object):
    def minCuttingCost(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        if m<=k and n<=k:
            return 0
        return k*(max(m,n)-k)