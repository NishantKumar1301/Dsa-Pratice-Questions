#Question : Maximum Profit from Trading Stocks with Discounts
#Link to the question: https://leetcode.com/contest/weekly-contest-451/problems/maximum-profit-from-trading-stocks-with-discounts/?slug=resulting-string-after-adjacent-removals&region=global_v2

from collections import defaultdict
class Solution(object):
    def dfs(self, u, freq, budget, present, future, MINI):
        dp = [self.dfs(child, freq, budget, present, future, MINI) for child in freq[u]]
        a,b = [MINI] * (budget + 1),[MINI] * (budget + 1)
        for v in range(2):  
            x = [MINI] * (budget + 1)
            y = [MINI] * (budget + 1)
            x[0] = 0
            c = present[u - 1] // 2 if v else present[u - 1]
            profit = future[u - 1] - c
            if c <= budget:
                y[c] = profit
            for c0, c1 in dp:
                x1 = [MINI] * (budget + 1)
                y1 = [MINI] * (budget + 1)
                for i in range(budget + 1):
                    if x[i] > MINI:
                        for j in range(budget - i + 1):
                            if c0[j] > MINI:
                                x1[i + j] = max(x1[i + j], x[i] + c0[j])
                for i in range(budget + 1):
                    if y[i] > MINI:
                        for j in range(budget - i + 1):
                            if c1[j] > MINI:
                                y1[i + j] = max(y1[i + j], y[i] + c1[j])
                x, y = x1, y1
            dp1 = b if v else a
            for i in range(budget + 1):
                dp1[i] = max(x[i], y[i])
        return (a, b)

    def maxProfit(self, n, present, future, hierarchy, budget):
        """
        :type n: int
        :type present: List[int]
        :type future: List[int]
        :type hierarchy: List[List[int]]
        :type budget: int
        :rtype: int
        """
        freq = defaultdict(list)
        for p, c in hierarchy:
            freq[p].append(c)
        MINI = -10**9
        ans = self.dfs(1, freq, budget, present, future, MINI)[0]
        return max(ans)