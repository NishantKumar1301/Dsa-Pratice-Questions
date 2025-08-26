#Question : Maximum Area of Longest Diagonal Rectangle
#Link to the question: https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle
class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        maxDiagonal = 0
        maxArea = 0
        for dimension in dimensions:
            l , b = dimension[0],dimension[1]
            d = l**2+b**2
            if d>maxDiagonal:
                maxDiagonal=d
                maxArea = l*b
            elif d==maxDiagonal:
                maxArea = max(l*b,maxArea)
        return maxArea