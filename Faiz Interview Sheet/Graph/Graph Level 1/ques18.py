#Question : Find Eventual Safe States
#Link to the question: https://leetcode.com/problems/find-eventual-safe-states/
from collections import deque
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        adj =[[] for _ in range(n)]
        indegree = [0]*n
        visited = [False]*n
        queue = deque()
        #Create a reversed graph
        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i]+=1
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            visited[curr]=True
            for node in adj[curr]:
                indegree[node]-=1
                if indegree[node]==0:
                    queue.append(node)
        ans = []
        for i in range(n):
            if visited[i]:
                ans.append(i)
        ans.sort()
        return ans
