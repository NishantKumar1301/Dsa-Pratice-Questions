#Question : Minimum Cost to Make at Least One Valid Path in a Grid
#Link to the question: https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/

from heapq import heappush,heappop
class Solution(object):
    def isValid(self,x,y,row,col):
        if 0<=x<row and 0<=y<col:
            return True
        else:
            return False

    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row,col = len(grid),len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        pq = []
        dx,dy = [0,0,1,-1],[1,-1,0,0]
        heappush(pq,(0,0,0))#(cost,x,y)
        while pq:
            cost,x,y = heappop(pq)
            if visited[x][y]:
                continue
            if x==row-1 and y==col-1:
                return cost
            visited[x][y]=True
            for dir in range(4): #Direction =Left,Right,Up,Down
                new_x = x+dx[dir]
                new_y = y + dy[dir]
                if self.isValid(new_x,new_y,row,col):
                    new_cost = cost
                    if dir+1!=grid[x][y]:
                        new_cost+=1
                    heappush(pq,(new_cost,new_x,new_y))
        return 0

