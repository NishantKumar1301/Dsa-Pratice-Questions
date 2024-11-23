#Question : Stock Buy and Sell – Multiple Transaction Allowed
#Link to the question: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/stock-buy-and-sell2615

class Solution:
    def maximumProfit(self, prices):
        n = len(prices)
        ahead = [0, 0]  
        cur = [0, 0]
        
        ahead[0] = ahead[1] = 0
        
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0
                
                if buy == 0:
                    profit = max(0 + ahead[0], -prices[ind] + ahead[1])
                elif buy == 1:
                    profit = max(0 + ahead[1], prices[ind] + ahead[0])
                cur[buy] = profit  
            
            ahead = cur  
        
        return cur[0]




