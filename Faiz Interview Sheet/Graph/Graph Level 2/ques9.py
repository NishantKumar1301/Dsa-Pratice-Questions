#Question : Number of Ways to Arrive at Destination
#Link to the question: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

MOD = 10**9+7
from heapq import heappush ,heappop

class Solution:
    def countPaths(self, n, roads):
        adj =[[] for _ in range(n)]
        for road in roads:
            u,v,w = road[0],road[1],road[2]
            adj[u].append((v,w))
            adj[v].append((u,w))
        dist = [float('inf')]*n
        dist[0]=0
        pq =[(0,0)]#dist,src
        ways = [0]*n
        ways[0]=1
        while pq :
            dis,node = heappop(pq)
            for ngbr,edgeWeight in adj[node]:
                #Case 1 : the neighbour node is visited at the first time
                if dis+edgeWeight<dist[ngbr]:
                    dist[ngbr]=dis+edgeWeight
                    heappush(pq,(dist[ngbr],ngbr))
                    ways[ngbr]=ways[node]
                #Case 2 : The nbr is visited by another route at the same minimum dsitance
                elif dis+edgeWeight == dist[ngbr]:
                    ways[ngbr]=(ways[ngbr]+ways[node] ) %MOD
        return ways[n-1] % MOD