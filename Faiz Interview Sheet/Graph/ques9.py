#Question : Directed Graph Cycle
#Link to the question: https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

class Solution:
    def dfs(self,src,adj,visited,pathVisited):
        visited[src]=True
        pathVisited[src]=True
        for node in adj[src]:
            if not visited[node]:
                if self.dfs(node,adj,visited,pathVisited):
                    return True
            elif pathVisited[node]:
                return True
        pathVisited[src]=False
        return False
    def isCycle(self, n, edges):
        # code here
        adj =[[] for _ in range(n)]
        visited = [False]*n
        pathVisited = [False]*n
        for edge in edges:
            u,v = edge[0],edge[1]
            adj[u].append(v)
        for i in range(n):
            if not visited[i]:
                if self.dfs(i,adj,visited,pathVisited):
                    return True
        return False