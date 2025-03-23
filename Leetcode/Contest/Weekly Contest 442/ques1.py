#Question : Maximum Containers on a Ship
#Link to the question: https://leetcode.com/contest/weekly-contest-442/problems/maximum-containers-on-a-ship/description/

class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        cells = n *n
        ans = 0 
        if cells *w <=maxWeight:
            ans = cells
        else :
            ans = maxWeight//w
        return ans

