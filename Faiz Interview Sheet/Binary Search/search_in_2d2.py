#Question : Search a 2D Matrix II
#Link to the question: https://leetcode.com/problems/search-a-2d-matrix-ii/
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n,m = len(matrix),len(matrix[0])
        row,col = 0 , m-1
        while row<n and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                row+=1
            else:
                col-=1
        return False