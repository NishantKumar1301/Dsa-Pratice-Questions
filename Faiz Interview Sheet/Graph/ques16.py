#Question : Course Schedule
#Link to the question: https://leetcode.com/problems/course-schedule/
from collections import deque
class Solution(object):
    def topologicalSort(self,adj,indegree):
        n = len(indegree)
        queue = deque()
        cnt =0
        for i in range(n):
            if indegree[i]==0:
                cnt+=1
                queue.append(i)
        while queue:
            curr = queue.popleft()
            for node in adj[curr]:
                indegree[node]-=1
                if indegree[node]==0:
                    cnt+=1
                    queue.append(node)
        if cnt==n: #That means we have visited all the node and no cycle is there
            return True
        else: #Indicates that we have been looped in a cycle
            return False 

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = [[]  for _ in range(numCourses)]
        indegree =[0]*numCourses
        for edge in prerequisites: # b->a connection
            a = edge[0]
            b = edge[1]
            adj[b].append(a)
            indegree[a]+=1
        return self.topologicalSort(adj,indegree)
        