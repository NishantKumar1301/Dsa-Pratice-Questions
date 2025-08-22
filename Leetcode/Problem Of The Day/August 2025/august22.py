#Question : Find the Minimum Area to Cover All Ones I
#Link to the question:  https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/
class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        minRow,maxRow,minCol,maxCol = m,-1,n,-1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    minRow = min(minRow,i)
                    maxRow = max(maxRow,i)
                    minCol = min(minCol,j)
                    maxCol = max(maxCol,j)
        ans = (maxRow-minRow+1)*(maxCol-minCol+1)
        return ans