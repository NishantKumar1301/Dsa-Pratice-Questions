#Question : Largest Rectangle in Histogram
#Link to the question: https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Area =max(area,(nse-pse-1)*nums[i])
        stack = []
        n = len(heights)
        maxi = float('-inf')
        for i in range(n):
            """
            If the top of the stack is greater than the curr element then do the following: 
            1. Find the index of next greater element , which is i
            2. Find the index of previous smaller element which is stack[-1] or -1 if len==0
            3. Compute  Area =max(area,(nse-pse-1)*nums[i])
            """
            while len(stack)>0 and heights[stack[-1]]>heights[i]:
                curr_idx = stack.pop()
                nse = i
                pse = -1 if len(stack)==0 else stack[-1]
                area = heights[curr_idx]*(nse-pse-1)
                maxi = max(area,maxi)
            stack.append(i)
            
        """
        After doing the above operations if still there are some elements left in the stack then do the following :
        1. pop out the current index element from the stack and finds its nse and pse 
        2. nse = n
        3. pse = stack[-1] if len(stack)>0 else -1
        4. area = max (area,heights[curr_idx]*(nse-pse-1))
        """
        while len(stack)>0:
            curr_idx = stack.pop()
            nse = n
            pse = -1 if len(stack)==0 else stack[-1]
            area = heights[curr_idx]*(nse-pse-1)
            maxi = max(area,maxi)
        
        return maxi