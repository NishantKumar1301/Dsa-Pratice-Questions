#Question : Longest Cycle in a Graph
#Link to the question: https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution(object):
    def dfs(self,src,adj,visited,pathVisited,dist,ans):
        if adj[src]!=-1:
            visited[src]=True
            pathVisited[src]=True
            for node in adj[src]:
                if (node!=-1 and not visited[node]): #Means that the node have not been visited so do dfs and update dist
                    dist[node]=dist[src]+1
                    self.dfs(node,adj,visited,pathVisited,dist,ans)
                elif (node!=-1 and pathVisited[node]):#Cycle detected so update ans 
                    ans[0]= max(ans[0],dist[src]-dist[node]+1)
            pathVisited[src]=False

    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        n = len(edges)
        adj =[[] for _ in range(n)]
        for i in range(n):
            if edges[i]!=-1:
                adj[i].append(edges[i])
        visited = [False]*n
        pathVisited = [False]*n
        dist = [0]*n
        ans =[-1]
        for i in range(n):
            if not visited[i]:
                dist[i]=1
                self.dfs(i,adj,visited,pathVisited,dist,ans)
        return ans[0]
        