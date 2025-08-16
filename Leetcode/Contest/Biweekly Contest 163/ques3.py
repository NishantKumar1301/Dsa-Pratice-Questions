#Question : Minimum Cost Path with Edge Reversals
#Link to the question: https://leetcode.com/contest/biweekly-contest-163/problems/minimum-cost-path-with-edge-reversals/

from heapq import heappush , heappop
class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for edge in edges:
            u,v,w = edge[0],edge[1],edge[2]
            adj[u].append((v,w))
            adj[v].append((u,2*w))
        dist = [float('inf')]*n
        dist[0]=0
        pq = []
        heappush(pq,(0,0))#(dist,node)
        while pq:
            currdist , node = heappop(pq)
            if currdist!=dist[node]:
                continue
            for ngbr, wt in adj[node]:
                new_dist = currdist+wt
                if new_dist<dist[ngbr]:
                    dist[ngbr]= new_dist
                    heappush(pq,(new_dist,ngbr))
        if dist[n-1]==float('inf'):
            return -1
        else:
            return dist[n-1]