#Question : Is Graph Bipartite?
#Link to the question: https://leetcode.com/problems/is-graph-bipartite/

class Solution(object):
    def dfs(self,src,col,adj,visited,color):
        visited[src]=True
        color[src]=col
        for node in adj[src]:
            if not visited[node]:
                if self.dfs(node,~col,adj,visited,color)==False:
                    return False
            elif color[node]==col:
                return False
        return True

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        visited = [False]*n
        color = [0]*n #0=red, 1 = pink
        for i in range(n):
            if not visited[i]:
                if self.dfs(i,1,graph,visited,color)==False:
                    return False
        return True
        