#Question : Largest Triangle Area
#Link to the question: https://leetcode.com/problems/largest-triangle-area

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        maxArea = float("-inf")
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    x1 = points[i][0]
                    y1 = points[i][1]

                    x2 = points[j][0]
                    y2 = points[j][1]

                    x3 = points[k][0]
                    y3 = points[k][1]

                    tempArea = abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
                    maxArea = max(maxArea,0.5*tempArea)
        return maxArea