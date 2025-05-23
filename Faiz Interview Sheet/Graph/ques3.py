#Question : Reorder Routes to Make All Paths Lead to the City Zero
#Link to the question: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/

class Solution(object):
    def dfs(self,src,parent,adj,visited,ans):
        visited[src]=True
        for child,weight in adj[src]:
            if not visited[child]:
                ans[0]+=weight
                self.dfs(child,src,adj,visited,ans)
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for edge in connections:
            u,v = edge[0],edge[1]
            adj[u].append((v,1))
            adj[v].append((u,0))
        visited=[False]*n
        ans=[0]
        self.dfs(0,-1,adj,visited,ans)
        return ans[0]
        
