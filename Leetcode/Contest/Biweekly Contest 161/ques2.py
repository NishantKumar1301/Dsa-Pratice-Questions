#Question : Count Islands With Total Value Divisible by K
#Link to the question:https://leetcode.com/contest/biweekly-contest-161/problems/count-islands-with-total-value-divisible-by-k/
from collections import deque
class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        queue = deque()
        m,n,ans = len(grid),len(grid[0]),0
        dx,dy = [0, 1, 0, -1]  , [1, 0, -1, 0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    total = 0
                    queue.append((i, j))
                    total += grid[i][j]
                    grid[i][j] = 0
                    while queue:
                        x, y = queue.popleft()
                        for dir in range(4):
                            nx = x + dx[dir]
                            ny = y + dy[dir]
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                                total += grid[nx][ny]
                                queue.append((nx, ny))
                                grid[nx][ny] = 0
                    if total % k == 0:
                        ans += 1
        return ans