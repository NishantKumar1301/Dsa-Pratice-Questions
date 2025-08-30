#Question : Valid Sudoku
#Link to the question: https://leetcode.com/problems/valid-sudoku/
class Solution(object):
    def traverse(self,sr,er,sc,ec,grid):
        s = set()
        for i in range(sr,er):
            # s = set()
            for j in range(sc,ec):
                if grid[i][j]=='.':
                    continue
                if grid[i][j] in s:
                    return False
                s.add(grid[i][j])
        return True

    def isValidSudoku(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m,n = len(grid),len(grid[0])
        #Validate the rows
        for i in range(9):
            s = set()
            for j in range(9):
                if grid[i][j]=='.':
                    continue
                if grid[i][j] in s:
                    return False
                s.add(grid[i][j])
        
        #Validate the columns
        for j in range(9):
            s = set()
            for i in range(9):
                if grid[i][j]=='.':
                    continue
                if grid[i][j] in s:
                    return False
                s.add(grid[i][j])
        
        #Validate the individual grids
        for row in range(0,9,3):
            er = row+3
            for col in range(0,9,3):
                ec = col+3

                if not self.traverse(row,er,col,ec,grid):
                    return False
        return True

