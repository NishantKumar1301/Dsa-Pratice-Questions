#Question : Grid Teleportation Traversal
#Link to the question : https://leetcode.com/contest/weekly-contest-450/problems/grid-teleportation-traversal/?slug=minimum-swaps-to-sort-by-digit-sum&region=global_v2

from collections import  defaultdict
import heapq
from collections import defaultdict
class Solution(object):
    def minMoves(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        m, n,dirs = len(grid), len(grid[0]),[(-1, 0), (1, 0), (0, -1), (0, 1)]
        freq,pq,visited = defaultdict(list),[],[[False] * n for _ in range(m)]
        heapq.heappush(pq, (0, 0, 0))
        for i in range(m):
            for j in range(n):
                char = grid[i][j]
                if char.isupper():
                    freq[char].append((i, j))
        while pq:
            cnt, x, y = heapq.heappop(pq)
            if visited[x][y]:
                continue
            visited[x][y] = True
            if x == m - 1 and y == n - 1:
                return cnt
            char = grid[x][y]
            if char.isupper():
                for a, b in freq[char]:
                    if not visited[a][b] and (a != x or b != y):
                        heapq.heappush(pq, (cnt, a, b))
                freq[char] = [] 
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y] and grid[new_x][new_y] != '#':
                    heapq.heappush(pq, (cnt + 1, new_x, new_y))
        return -1
