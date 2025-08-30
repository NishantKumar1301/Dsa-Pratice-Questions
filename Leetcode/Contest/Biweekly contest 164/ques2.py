#Question : Twisted Mirror Path Count
#Link to the question: https://leetcode.com/contest/biweekly-contest-164/problems/twisted-mirror-path-count/
MOD = 10**9 + 7
class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        left , right = [[(-2, -2) for _ in range(n)] for _ in range(m)] , [[(-2, -2) for _ in range(n)] for _ in range(m)]
        def helper(x, y, d):
            if x < 0 or x >= m or y < 0 or y >= n:
                return (-1, -1)
            if d == 0:
                if left[x][y][0] != -2:
                    return left[x][y]
                if grid[x][y] == 0:
                    left[x][y] = (x, y)
                    return left[x][y]
                left[x][y] = helper(x + 1, y, 1)
                return left[x][y]
            else:
                if right[x][y][0] != -2:
                    return right[x][y]
                if grid[x][y] == 0:
                    right[x][y] = (x, y)
                    return right[x][y]
                right[x][y] = helper(x, y + 1, 0)
                return right[x][y]
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                ans = 0
                arr = helper(i, j + 1, 0)
                if arr[0] != -1:
                    ans += dp[arr[0]][arr[1]]
                arr1 = helper(i + 1, j, 1)
                if arr1[0] != -1:
                    ans += dp[arr1[0]][arr1[1]]
                dp[i][j] = ans % MOD
        return dp[0][0]