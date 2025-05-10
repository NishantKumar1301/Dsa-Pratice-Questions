class Solution(object):
    def maxWeight(self, n, edge, p, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :type t: int
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for i, j, w in edge:
            adj[j].append((i, w))
        dp = [set([0]) for _ in range(n)]
        for _ in range(p):
            dp1 = [set() for _ in range(n)]
            for node in range(n):
                for ngbr, cost in adj[node]:
                    for total in dp[ngbr]:
                        combined = total + cost
                        if combined < k:
                            dp1[node].add(combined)
            dp = dp1
        ans = -1
        for node in range(n):
            for val in dp[node]:
                if val < k:
                    ans = max(ans, val)
        return ans