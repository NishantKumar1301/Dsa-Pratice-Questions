#Question : Undirected Graph Cycle
#Link to the question: https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/0

class Solution:
    def dfs(self,src,parent,adj,visited):
        visited[src]=True
        for node in adj[src]:
            if not visited[node]:
                if self.dfs(node,src,adj,visited)==True:
                    return True
            elif node!=parent:
                return True
        return False

    def isCycle(self, n, edges):
        #Code here
        adj =[[] for _ in range(n)]
        visited =[False]*n
        for edge in edges:
            u,v = edge[0]-1,edge[1]-1
            adj[u].append(v)
            adj[v].append(u)
        for i in range(n):
            if not visited[i]:
                if self.dfs(i,-1,adj,visited)==True:
                    return True
        return False
