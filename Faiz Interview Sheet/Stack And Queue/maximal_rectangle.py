#Question :  Maximal Rectangle
#Link to the question: https://leetcode.com/problems/maximal-rectangle/
class Solution(object):
    def largestRectangleArea(self,nums):
        stack = []
        n = len(nums)
        maxi = 0
        for i in range(n):
            while len(stack)>0 and nums[stack[-1]]>nums[i]:
                idx = stack.pop()
                nse =i
                pse = -1 if len(stack)==0 else stack[-1]
                maxi = max(maxi ,nums[idx]*(nse-pse-1))
            stack.append(i)
        while len(stack)>0:
            idx = stack.pop()
            nse =n
            pse = -1 if len(stack)==0 else stack[-1]
            maxi = max(maxi ,nums[idx]*(nse-pse-1))
        return maxi

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m,n = len(matrix),len(matrix[0])
        maxi = 0
        prefix_sum = [[0]*n for _ in range(m)]
        #Compute the prefix array
        for col in range(n):
            total_one = 0
            for row in range(m):
                total_one+=int(matrix[row][col])
                if matrix[row][col]=='0':
                    total_one = 0
                prefix_sum[row][col]=total_one
        for row in prefix_sum:
            maxArea = self.largestRectangleArea(row)
            maxi = max(maxi,maxArea)
        return maxi
        