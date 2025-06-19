#Question : Course Schedule II
#Link to the question:https://leetcode.com/problems/course-schedule-ii/
from collections import deque
class Solution(object):
    def topologicalSort(self,adj,indegree):
        n = len(indegree)
        ans =[]
        cnt =0 
        queue = deque()
        for i in range(n):
            if indegree[i]==0:
                cnt+=1
                queue.append(i)
                ans.append(i)
        while queue:
            curr = queue.popleft()
            for node in adj[curr]:
                indegree[node]-=1
                if indegree[node]==0:
                    ans.append(node)
                    queue.append(node)
                    cnt+=1
        if cnt==n : #Every node is visited and there is no cycle 
            return ans
        else: #Cycle have been detected
            return []
    def findOrder(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj =[[] for _ in range(n)]
        indegree =[0]*n
        for edge in prerequisites:
            a,b = edge[0],edge[1] #b---a
            adj[b].append(a)
            indegree[a]+=1
        ans = self.topologicalSort(adj,indegree)
        return ans
