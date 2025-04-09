#Question : Final Prices With a Special Discount in a Shop
#Link to the question: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/?envType=daily-question&envId=2024-12-18

class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        #Method1 : Brute Force approach
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[j]<=prices[i]:
        #             prices[i]-=prices[j]
        #             break
        # return prices

        #Method2 : Using Stack
        n = len(prices)
        stack =[]
        for i in range(n-1,-1,-1):
            while stack and stack[-1]>prices[i]: #stack[-1]=It is similar as stack.peek() in java, it removes and returns the top element
                stack.pop()
            final_prices = prices[i] if not stack else prices[i]-stack[-1]
            stack.append(prices[i])
            prices[i]=final_prices
        return prices        

