#Question : Map of Highest Peak
#Link to the question: https://leetcode.com/problems/map-of-highest-peak/description/

from collections import deque
class Solution(object):
    def isValid(self,x,y,m,n):
        return 0<=x<m and 0<=y<n
    
    def highestPeak(self, grid):
        m , n = len(grid) , len(grid[0])
        ans = [[0]*n for _ in range(m)]
        visited = [[False]*n for _ in range(m)]
        level =0
        queue = deque()
        dirX, dirY = [0,0,1,-1],[1,-1,0,0]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    queue.append((i,j))
                    visited[i][j]=True 
        while queue:
            size = len(queue)
            for _ in range(size):
                x,y = queue.popleft()
                for dir in range(4):
                    new_x , new_y = x+dirX[dir], y+dirY[dir]
                    if self.isValid(new_x,new_y,m,n) and not visited[new_x][new_y]:
                        queue.append((new_x,new_y))
                        ans[new_x][new_y]=1+level
                        visited[new_x][new_y]=True
            level+=1
        
        return ans
        


