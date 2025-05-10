#Question : Maximum Weighted K-Edge Path
#Link to the question: https://leetcode.com/contest/biweekly-contest-156/problems/maximum-weighted-k-edge-path/description/?slug=minimum-operations-to-convert-all-elements-to-zero&region=global_v2

class Solution(object):
    def maxWeight(self, n, edges, k, t):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :type t: int
        :rtype: int
        """
        adj = []
        for _ in range(n):
            adj.append([])
        for u, v, w in edges:
            adj[u].append((v, w))
        dp = [[-1] * n for _ in range(k + 1)]
        for j in range(n):
            dp[0][j] = 0
        for i in range(1, k + 1):
            for j in range(n):
                if dp[i - 1][j] >= 0:
                    for v, w in adj[j]:
                        total = dp[i - 1][j] + w
                        if total < t:
                            dp[i][v] = max(dp[i][v], total)
        ans = -1
        for i in range(n):
            ans = max(ans, dp[k][i])
        return ans