#Question : Put Marbles in Bags
#Link to the question: https://leetcode.com/problems/put-marbles-in-bags/description/?envType=daily-question&envId=2025-03-31

class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :r type: int
        """
        n = len(weights)
        m = n -1
        pair = [0]*m
        for i in range(m):
            pair[i]=weights[i]+weights[i+1]
        pair.sort()
        mini=maxi =0
        for i in range(k-1):
            mini+=pair[i]
            maxi+=pair[m-i-1]
        return maxi - mini

