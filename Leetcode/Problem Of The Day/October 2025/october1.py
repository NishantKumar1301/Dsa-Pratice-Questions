#Question : Water Bottles
#Link to the question: https://leetcode.com/problems/water-bottles
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        n = 0
        while numBottles>=numExchange:
            n+=numExchange
            numBottles-=numExchange
            numBottles+=1
        return n+numBottles