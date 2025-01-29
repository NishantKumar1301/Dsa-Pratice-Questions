#Question : Redundant Connection
#Link to the question: https://leetcode.com/problems/redundant-connection/description/

class Solution(object):
    def find_parent(self, parent, v):
        if parent[v]==-1:
            return v
        parent[v]= self.find_parent(parent, parent[v])
        return parent[v]

    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = [-1]*(n+1)
        for edge in edges:
            parent_x = self.find_parent(parent,edge[0])
            parent_y = self.find_parent(parent,edge[1])
            if parent_x == parent_y:
                return edge
            else:
                parent[parent_x]=parent_y
        return [0,0]
        
