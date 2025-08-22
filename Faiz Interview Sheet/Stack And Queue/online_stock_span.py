#Question : Online Stock Span
#Link to the question: https://leetcode.com/problems/online-stock-span/

class StockSpanner(object):

    def __init__(self):
        self.stack = [] # store the (stock , no of previous minimum)

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        #prev = 1 bcoz in this the current stock has a value of 1
        prev = 1
        while self.stack and self.stack[-1][0]<=price:
            #Update the number of previous minimums
            prev+=self.stack[-1][-1]
            self.stack.pop()
        #Append the new previous and the element
        self.stack.append((price,prev))
        return prev
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)