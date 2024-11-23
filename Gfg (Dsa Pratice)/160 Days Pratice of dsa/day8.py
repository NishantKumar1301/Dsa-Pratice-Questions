#Question : Stock Buy and Sell – Max one Transaction Allowed
#Link to the question: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/buy-stock-2

class Solution:
    def maximumProfit(self, prices):
        # code here
        mini ,profit= prices[0],0
        n = len(prices)
        for i in range(n):
            cost = prices[i]-mini
            profit = max(profit,cost)
            mini = min(mini,prices[i])
        return profit
        

