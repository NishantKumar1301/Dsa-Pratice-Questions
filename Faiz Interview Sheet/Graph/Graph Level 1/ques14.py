#Question : Topological sort
#Link to the question:https://www.geeksforgeeks.org/problems/topological-sort/1
class Solution:
    def topoSort(self, n, edges):
        # Code here
        adj =[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
        visited = [False]*n
        stack =[]
        for i in range(n):
            if not visited[i]:
                self.dfs(i,visited,stack,adj)
        #Return the reversed stack
        return stack[::-1]
    
    def dfs(self, src,visited,stack,adj):
        visited[src]=True
        for node in adj[src]:
            if not visited[node]:
                self.dfs(node,visited,stack,adj)
        stack.append(src)