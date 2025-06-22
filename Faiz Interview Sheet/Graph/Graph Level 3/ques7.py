#Question : Minimum Spanning Tree
#Link to the question:  https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1

from heapq import heappush,heappop
from typing import List
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        mst = []
        visited = [False]*V
        pq = [(0,0,-1)]#wt,node,parent
        total =0
        while pq:
            wt,node,parent= heappop(pq)
            if visited[node]:
                continue
            visited[node]=True
            total+=wt
            if parent!=-1:
                mst.append((parent,node))
            for adjNode,edgeWt in adj[node]:
                if not visited[adjNode]:
                    heappush(pq,(edgeWt,adjNode,node))
        
        #If we have to print the mst
        for u,v in mst:
            print(u,v)

        return total