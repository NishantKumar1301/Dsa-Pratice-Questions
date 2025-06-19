#Question : Shortest Cycle in a Graph
#Link to the question: https://leetcode.com/problems/shortest-cycle-in-a-graph/

from collections import deque
class Solution(object):
    def bfs(self,src,adj,visited,dist,ans):
        queue = deque()
        visited[src]=True
        dist[src]=0
        queue.append((src,-1))#(node,parent)
        while queue:
            curr,parent = queue.popleft()
            for node in adj[curr]:
                if not visited[node]:
                    visited[node]=True
                    dist[node]=dist[curr]+1
                    queue.append((node,curr))
                elif node!=parent: #cycle have been detected, bcoz it have not been visted and node!=parent
                    ans[0]= min(ans[0],dist[curr]+dist[node]+1)

    def findShortestCycle(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for edge in edges:
            u,v= edge[0],edge[1]
            adj[u].append(v)
            adj[v].append(u)
        ans=[float('inf')]
        for i in range(n):
            visited = [False]*n
            dist = [int(1e9)]*n
            self.bfs(i,adj,visited,dist,ans)
        return -1 if ans[0]==float('inf') else ans[0]