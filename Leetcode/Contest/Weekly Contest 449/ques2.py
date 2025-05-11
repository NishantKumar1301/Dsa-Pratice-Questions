#Question : Equal Sum Grid Partition I
#Link to the question: https://leetcode.com/contest/weekly-contest-449/problems/equal-sum-grid-partition-i/description/?slug=minimum-deletions-for-at-most-k-distinct-characters&region=global_v2

class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        row_total, column_total = [], []
        for row in grid:
            row_total.append(sum(row))
        for j in range(n):
            sum_ = 0
            for i in range(m):
                sum_ += grid[i][j]
            column_total.append(sum_)
        total = sum(row_total)
        curr = 0
        for i in range(m - 1):
            curr += row_total[i]
            if curr == total - curr:
                return True
        total = sum(column_total)
        curr = 0
        for i in range(n - 1):
            curr += column_total[i]
            if curr == total - curr:
                return True
        return False
