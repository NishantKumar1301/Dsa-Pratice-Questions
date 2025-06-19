#Question : Parallel Courses III
#Link to the question: https://leetcode.com/problems/parallel-courses-iii/
from collections import deque
class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        queue = deque()
        adj =[[] for _ in range(n)]
        indegree=[0]*n
        dist = [0]*n
        for relation in relations:
            u= relation[0]-1
            v = relation[1]-1
            adj[u].append(v)
            indegree[v]+=1
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
                dist[i]=time[i]
        while queue:
            curr = queue.popleft()
            for node in adj[curr]:
                dist[node]= max(dist[node],dist[curr]+time[node])
                indegree[node]-=1
                if indegree[node]==0:
                    queue.append(node)
        return max(dist)

