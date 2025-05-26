#Question : Largest Color Value in a Directed Graph
#Link to the question: https://leetcode.com/problems/largest-color-value-in-a-directed-graph/?envType=daily-question&envId=2025-05-26

class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(colors)
        adj =[[] for _ in range(n)]
        for edge in edges:
            u,v=edge[0],edge[1]
            adj[u].append(v)
        visited =[0]*n # 0-Unvisited, 1 - visited and processing , 2-visited and procesed
        longest =[[0]*n for _ in range(26)]#longest[i][j]=X means total x number of total node i from current node j
        ans =0
        for i in range(n):
            res = self.dfs(i,adj,visited,longest,colors)
            if res==float('inf'): #Cycle detection
                return -1
            ans = max(ans,res)
        return ans


    def dfs(self,src,adj,visited,longest,colors):
        if visited[src]==1: #cycle detected
            return float('inf')
        if visited[src]==0:
            visited[src]=1
            for node in adj[src]:
                res = self.dfs(node,adj,visited,longest,colors)
                if res==float('inf'):
                    return float('inf')
                #Now update colors of every character(a-z) for each node
                for i in range(26):
                    longest[i][src]=max(longest[i][src],longest[i][node])
            #Update the color by considering current node 
            longest[ord(colors[src])-ord('a')][src]+=1
            #Mark the src as visited and processed
            visited[src]=2
        #Return max value from the longest table
        return longest[ord(colors[src])-ord('a')][src]

