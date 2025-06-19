#Question : Dijkstra Algorithm
#Link to the question:https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1


from heapq import heappush , heappop
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, n, edges, src):
        # code here
        adj =[[] for _ in range(n)]
        for edge in edges:
            u,v,w = edge[0],edge[1],edge[2]
            adj[u].append((v,w))
            adj[v].append((u,w))
        dist = [float('inf')]*n
        dist[src]=0
        pq = [(0,src)] #(dist,node)
        while pq:
            dis , node = heappop(pq)
            for item in adj[node]:
                adjNode = item[0]
                edgeWeight = item[1]
                if dis+edgeWeight<dist[adjNode]:
                    dist[adjNode]=dis+edgeWeight
                    heappush(pq,(dist[adjNode],adjNode))
        # if dist[n-1]==float('inf'):
        #     return -1 # Have commented this out bcoz in this destination is not defined
        return dist