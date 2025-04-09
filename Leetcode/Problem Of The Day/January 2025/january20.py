#Question : First Completely Painted Row or Column
#Link to the question: https://leetcode.com/problems/first-completely-painted-row-or-column/description/

class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        lookup = {}
        for i in range(m):
            for j in range(n):
                lookup[mat[i][j]]=(i,j)
        row_count,col_count =[0]*m,[0]*n
        for i , val in enumerate(arr):
            x,y = lookup[val]
            row_count[x]+=1
            col_count[y]+=1
            if row_count[x]==n or col_count[y]==m:
                return i
        return 0
        


