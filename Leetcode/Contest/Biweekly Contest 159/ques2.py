#Question : Find Maximum Area of a Triangle
#Link to the question:  https://leetcode.com/contest/biweekly-contest-159/problems/find-maximum-area-of-a-triangle/

class Solution(object):
    def maxArea(self, coords):
        """
        :type coords: List[List[int]]
        :rtype: int
        """
        coords.sort()
        ans = 0
        p,q,i,n = coords[0][0],coords[-1][0],0,len(coords)
        while i < n:
            x ,j= coords[i][0],i
            while i < len(coords) and coords[i][0] == x:
                i += 1
            if i - j > 1:
                height = abs(coords[j][1] - coords[i - 1][1])
                ans = max(ans, height * (q - x))
                ans = max(ans, height * (x - p))

        coords.sort(key=lambda x: x[1])
        p,q ,i= coords[0][1],coords[-1][1],0
        while i < n:
            y,j = coords[i][1],i
            while i < len(coords) and coords[i][1] == y:
                i += 1
            if i - j > 1:
                base = abs(coords[j][0] - coords[i - 1][0])
                ans = max(ans, base * (q - y))
                ans = max(ans, base * (y - p))
        if ans==0:
            return -1
        else:
            return ans