#Question :Minimum Time to Reach Destination in Directed Graph
#Link to the question:  https://leetcode.com/contest/biweekly-contest-160/problems/minimum-time-to-reach-destination-in-directed-graph/

from heapq import heappush , heappop
class Solution(object):
    def minTime(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for edge in edges:
            u,v,start,end = edge[0],edge[1],edge[2],edge[3]
            adj[u].append((v,start,end))

        dist = [-1]*n
        dist[0]=0
        pq =[(0,0)] #(time,node)
        while pq:
            time , node = heappop(pq)
            if dist[node]!=-1 and time > dist[node]:
                continue
            if node==n-1:
                return time
            for v, start , end in adj[node]:
                d = max(time, start)
                if d<=end:
                    a = d+1
                    if dist[v]==-1 or a < dist[v]:
                        dist[v]=a
                        heappush(pq,(a,v))
        return -1