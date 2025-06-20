#User function Template for python3
#Question : Bellman-Ford
#Link to the question:  https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        dist = [int(1e8)]*V
        dist[src]=0
        for _ in range(V-1):
            for u,v,w in edges:
                if dist[u]!=int(1e8) and dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w
        
        #Check for negative cycle  : If on nth iteration the value still changes then there is negative cycle
        for u,v,w in edges:
            if dist[u]!=int(1e8) and dist[u]+w<dist[v]:
                return [-1]
        return dist