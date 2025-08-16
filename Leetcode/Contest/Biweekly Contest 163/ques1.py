#Question : Minimum Sensors to Cover Grid
#Link to the question: https://leetcode.com/contest/biweekly-contest-163/problems/minimum-sensors-to-cover-grid/
class Solution(object):
    def minSensors(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        cnt = 2*k+1
        row,col = (n+cnt-1)//cnt,(m+cnt-1)//cnt
        return row*col