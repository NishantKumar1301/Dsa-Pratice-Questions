#Question : Number of Provinces
#Link to the question: https://leetcode.com/problems/number-of-provinces/description/

class Solution(object):
    def dfs(self,src,adj,visited):
        visited[src]=True
        for node in adj[src]:
            if not visited[node]:
                self.dfs(node,adj,visited)

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        #Calculate number of cities 
        n = len(isConnected)
        #Create an adjacency list
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1: #isConnected[i][j]==1 Means that they are connected
                    adj[i].append(j)
                    adj[j].append(i)
        
        visited = [False]*n
        cnt = 0
        for i in range(n):
            if not visited[i]:
                self.dfs(i,adj,visited)
                cnt+=1
        return cnt

