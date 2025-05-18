#Question : Grid Teleportation Traversal
#Link to the question : https://leetcode.com/contest/weekly-contest-450/problems/grid-teleportation-traversal/?slug=minimum-swaps-to-sort-by-digit-sum&region=global_v2

from collections import deque, defaultdict

class Solution(object):
    def minMoves(self, matrix):
        """
        :type matrix: List[str]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        voracelium = matrix  # Storing the input midway as per the question
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = [[False]*n for _ in range(m)]

        # Step 1: Collect all portal positions
        portals = defaultdict(list)
        for i in range(m):
            for j in range(n):
                c = matrix[i][j]
                if 'A' <= c <= 'Z':
                    portals[c].append((i, j))

        used_portals = set()
        queue = deque()
        queue.append((0, 0, 0))  # (x, y, moves)
        visited[0][0] = True

        while queue:
            x, y, steps = queue.popleft()

            if x == m - 1 and y == n - 1:
                return steps

            # Move to adjacent cells
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] != '#':
                    visited[nx][ny] = True
                    queue.append((nx, ny, steps + 1))

            # Teleport if it's a portal and we haven't used this letter yet
            cell = matrix[x][y]
            if 'A' <= cell <= 'Z' and cell not in used_portals:
                used_portals.add(cell)
                for tx, ty in portals[cell]:
                    if not visited[tx][ty]:
                        visited[tx][ty] = True
                        queue.appendleft((tx, ty, steps))  # Teleportation is free (no move)

        return -1  # Destination not reachable
