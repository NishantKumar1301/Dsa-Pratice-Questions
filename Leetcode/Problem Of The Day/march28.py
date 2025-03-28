#Question : Maximum Number of Points From Grid Queries
#Link to the question: https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/solutions/6505775/maximum-number-of-points-from-grid-queries/?envType=daily-question&envId=2025-03-28
import heapq

class Solution:
    def maxPoints(self, grid, queries):
        row_count, col_count = len(grid), len(grid[0])
        ans = [0] * len(queries)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])

        pq = []
        visited = [[False] * col_count for _ in range(row_count)]
        total = 0
        heapq.heappush(pq, (grid[0][0], 0, 0))
        visited[0][0] = True

        for val, idx in sorted_queries:
            while pq and pq[0][0] < val:
                _, row, col = heapq.heappop(pq)

                total += 1

                for row_offset, col_offset in dirs:
                    new_row, new_col = (
                        row + row_offset,
                        col + col_offset,
                    )
                    if (
                        new_row >= 0
                        and new_col >= 0
                        and new_row < row_count
                        and new_col < col_count
                        and not visited[new_row][new_col]
                    ):
                        heapq.heappush(pq, (grid[new_row][new_col], new_row, new_col))
                        visited[new_row][new_col] = True
            ans[idx] = total

        return ans