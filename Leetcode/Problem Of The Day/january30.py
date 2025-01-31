#Question : Making A Large Island
#Link to the question: https://leetcode.com/problems/making-a-large-island/description/?envType=daily-question&envId=2025-01-31


class Solution(object):
    def isValid(self, n, x, y):
        return 0 <= x < n and 0 <= y < n

    def markIsland(self, grid, island_number, n, x, y):
        grid[x][y] = island_number
        count = 1
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        for i in range(4):
            newX, newY = x + dx[i], y + dy[i]
            if self.isValid(n, newX, newY) and grid[newX][newY] == 1:
                count += self.markIsland(grid, island_number, n, newX, newY)
                
        return count

    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        island_size = {}
        island_number = 2

        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    island_size[island_number] = self.markIsland(grid, island_number, n, x, y)
                    island_number += 1

        max_size = 0
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    islands = set()
                    for i in range(4):
                        newX, newY = x + dx[i], y + dy[i]
                        if self.isValid(n, newX, newY):
                            islands.add(grid[newX][newY])
                    
                    curr_island = 1
                    for key in islands:
                        curr_island += island_size.get(key, 0)
                    
                    max_size = max(max_size, curr_island)

        return max_size if max_size != 0 else n * n


