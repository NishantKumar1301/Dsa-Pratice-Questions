#Question : Search a 2D Matrix
#Link to the question: https://leetcode.com/problems/search-a-2d-matrix/
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n,m = len(matrix),len(matrix[0])
        low = 0
        high = n*m-1
        while low<=high:
            mid = low+(high-low)//2
            #row position = mid // no of column = mid//m
            #Col position = mid % no of columns = mid % m
            row = mid//m
            col = mid % m
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                high-=1
            else:
                low+=1
        return False