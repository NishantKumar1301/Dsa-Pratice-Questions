#Question : 01 Matrix
#Link to the question: https://leetcode.com/problems/01-matrix/

from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n,m = len(mat),len(mat[0])
        visited =[[False]*m for _ in range(n)]
        ans = [[0]*m for _ in range(n)]
        dr,dc = [-1,0,1,0],[0,1,0,-1]
        queue = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    queue.append((i,j,0)) #row,col,step
                    visited[i][j]=True
        while queue:
            row,col,time = queue.popleft()
            ans[row][col]=time
            for i in range(4):
                nr,nc = row+dr[i],col+dc[i]
                if 0<=nr<n and 0<=nc<m and not visited[nr][nc]:
                    visited[nr][nc]=True
                    queue.append((nr,nc,time+1))
        return ans
