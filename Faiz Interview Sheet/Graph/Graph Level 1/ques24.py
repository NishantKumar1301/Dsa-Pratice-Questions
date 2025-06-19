#Question : Find All Groups of Farmland
#Link to the question: https://leetcode.com/problems/find-all-groups-of-farmland/
class Solution(object):
    def dfs(self,i,j,land,visited):
        m,n=len(land),len(land[0])
        dr ,dc =[-1,0,1,0],[0,1,0,-1]
        visited[i][j]=True
        r2,c2 = i,j
        for p in range(4):
            ni,nc=i+dr[p],j+dc[p]
            if 0<=ni<m and 0<=nc<n and not visited[ni][nc] and land[ni][nc]==1:
                nr2 ,nc2 = self.dfs(ni,nc,land,visited)
                r2 = max(r2,nr2)
                c2 = max(c2,nc2)
        return r2,c2

    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n = len(land),len(land[0])
        ans= []
        visited =[[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and land[i][j]==1:
                    r1,c1 = i,j
                    r2,c2,=self.dfs(i,j,land,visited)
                    ans.append([r1,c1,r2,c2])
        return ans
        