#Question : Find a Peak Element II
#Link to the question: https://leetcode.com/problems/find-a-peak-element-ii/
class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        rows,cols = len(mat),len(mat[0])
        low = 0
        high = cols-1
        while low<=high:
            mid = low + (high-low)//2
            #Find the max row index in the particular column
            max_row =0
            for i in range(1,rows):
                if mat[i][mid]>mat[max_row][mid]:
                    max_row = i
            
            curr_val = mat[max_row][mid]
            left_val = mat[max_row][mid-1] if mid -1>=0 else -1
            right_val = mat[max_row][mid+1] if mid+1<cols else -1
            if curr_val>left_val and curr_val>right_val:
                return [max_row , mid]
            elif curr_val <left_val:
                high-=1
            else:
                low+=1
        return [-1,-1]