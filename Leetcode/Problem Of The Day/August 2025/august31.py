#Question : Sudoku Solver
#Link to the question: https://leetcode.com/problems/sudoku-solver/

class Solution(object):
    def isvalid(self,grid,row,col,d):
        #Check whether the given char is present in the row or col if so then return False
        for i in range(9):
            if grid[row][i]==d:
                return False
            if grid[i][col]==d:
                return False
        #Check whether the given char is present in the given grid
        start_i =(row//3)*3
        start_j = (col//3)*3
        for k in range(3):
            for l in range(3):
                if grid[start_i+k][start_j+l]==d:
                    return False
        return True
    

    def solve(self,grid):
        for i in  range(9):
            for j in range(9):
                if grid[i][j]=='.':
                    for char in '123456789':
                        if self.isvalid(grid,i,j,char):
                            grid[i][j]=char
                            if self.solve(grid):
                                return True
                            #Backtracking
                            grid[i][j]='.'
                    return False
        return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        return self.solve(board)