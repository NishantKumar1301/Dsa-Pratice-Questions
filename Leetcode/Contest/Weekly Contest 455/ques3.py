#Question : Minimum Increments to Equalize Leaf Paths
#Link to the question:  https://leetcode.com/contest/weekly-contest-455/problems/minimum-increments-to-equalize-leaf-paths/

class Solution(object):
    def dfs(self, node, parent, adj, cost):
        child = []
        for ngbr in adj[node]:
            if ngbr != parent:
                child.append(self.dfs(ngbr, node, adj, cost))
        
        if not child:
            return (cost[node], 0)  # Leaf node: (score, 0 increase)
        
        maxi = 0
        incr = 0
        for score, inc in child:
            incr += inc
            maxi = max(maxi, score)

        # Count how many child paths need increase to match maxi
        for score, _ in child:
            if score < maxi:
                incr += 1

        return (cost[node] + maxi, incr)

    def minIncrease(self, n, edges, cost):
        """
        :type n: int
        :type edges: List[List[int]]
        :type cost: List[int]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        return self.dfs(0, -1, adj, cost)[1]  