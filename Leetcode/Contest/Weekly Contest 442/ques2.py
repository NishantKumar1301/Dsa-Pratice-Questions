#Question : Properties Graph
#Link to the question: https://leetcode.com/contest/weekly-contest-442/problems/properties-graph/description/?slug=maximum-containers-on-a-ship&region=global_v2

class Solution:
    def intersect(self, a, b):
        return len(set(a) & set(b))
    
    def dfs(self, node, adj, seen):
        seen[node] = True
        for neighbor in adj[node]:
            if not seen[neighbor]:
                self.dfs(neighbor, adj, seen)

    def numberOfComponents(self, properties, k):
        """
        :type properties: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(properties)
        
        adj = [[] for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                if self.intersect(properties[i], properties[j]) >= k:
                    adj[i].append(j)
                    adj[j].append(i)
        seen = [False] * n
        ans = 0
        for i in range(n):
            if not seen[i]:
                self.dfs(i, adj, seen)
                ans += 1
        return ans

