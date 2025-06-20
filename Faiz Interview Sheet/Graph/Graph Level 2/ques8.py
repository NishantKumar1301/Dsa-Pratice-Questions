#Question : Network Delay Time
#Link to the question:  https://leetcode.com/problems/network-delay-time/

from heapq import heappush,heappop
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        #0 Based Indexing
        k-=1
        adj =[[] for _ in range(n)]
        for time in times:
            u,v,w = time[0]-1,time[1]-1,time[2]
            adj[u].append((v,w))
        dist = [float('inf')]*(n)
        dist[k]=0
        pq=[(0,k)]
        while pq:
            dis,node = heappop(pq)
            for adjNode,edgeWeight in adj[node]:
                if dis+edgeWeight<dist[adjNode]:
                    dist[adjNode]=dis+edgeWeight
                    heappush(pq,(dist[adjNode],adjNode))
        if max(dist)==float('inf'):
            return -1
        else:
            return max(dist)