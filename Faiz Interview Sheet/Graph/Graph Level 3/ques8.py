#Question : Minimum Spanning Tree - Kruskal's Algorithm
#Link to the question:  https://www.geeksforgeeks.org/problems/minimum-spanning-tree-kruskals-algorithm/1

#User function Template for python3
from typing import List

class Solution:

    def findParent(self,u,parent):
        if parent[u]!=u:
            parent[u]=self.findParent(parent[u],parent)
        return parent[u]

    def union(self,u,v,parent,size):
        pu,pv= self.findParent(u,parent),self.findParent(v,parent)
        if pu==pv:
            return 
        if size[pu]<size[pv]:
            parent[pu]=pv
            size[pv]+=size[pu]
        else:
            parent[pv]=pu
            size[pu]+=size[pv]

    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        # code here
        parent = list(range(V))
        size = [1]*V
        total =0
        #Sort the edges based on weight edges[2]=weight
        edges.sort(key = lambda x:x[2])
        for u,v,w in edges:
            if self.findParent(u,parent)!=self.findParent(v,parent):
                total+=w
                self.union(u,v,parent,size)
        return total