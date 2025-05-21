#Question : Set Matrix Zeroes
#Link to the question: https://leetcode.com/problems/set-matrix-zeroes/description/?envType=daily-question&envId=2025-05-21

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) # length of row
        m = len(matrix[0]) #Length of column
        row = [0]*n
        col =[0]*m
        for i in range (n):
            for j in range(m):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        for i in range (n):
            for j in range(m):
                if row[i]==1 or col[j]==1:
                    matrix[i][j]=0
        return matrix

