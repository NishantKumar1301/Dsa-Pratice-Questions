#Question : Unit Conversion I
#Link to the question: https://leetcode.com/contest/biweekly-contest-155/problems/unit-conversion-i/description/?slug=find-the-most-common-response&region=global_v2

MOD = 10**9 + 7

class Solution(object):
    def dfs(self, edge):
        for vert, fact in grid[edge]:
            if adj[vert] == -1:
                adj[vert] = (adj[edge] * fact) % MOD
                self.dfs(vert)
    
    def baseUnitConversions(self, conversions):
        """
        :type conversions: List[List[int]]
        :rtype: List[int]
        """
        global grid, adj
        n=0
        for edge in conversions:
            n = max(n, max(edge[0], edge[1]))
        n += 1
        grid = [[] for _ in range(n)]
        for u, v, fact in conversions:
            grid[u].append((v, fact))
        adj = [-1] * n
        adj[0] = 1
        
        self.dfs(0)
        ans = [int(x) for x in adj]
        return ans
