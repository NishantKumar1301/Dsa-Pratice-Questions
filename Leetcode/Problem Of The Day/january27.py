#Question : Course Schedule IV
#Link to the question: https://leetcode.com/problems/course-schedule-iv/description/?envType=daily-question&envId=2025-01-27

# #Method 1 : Using Bfs  : It will work if the number of query is less otherwise it would give tle
from collections import deque
class Solution(object):
    def bfs(self,start,target,adj,visited):
        queue = deque([start])
        while queue:
            currNode = queue.popleft()
            if currNode == target:
                return True
            if not visited[currNode]:
                visited[currNode]=True
                for neighbor in adj[currNode]:
                    queue.append(neighbor)
        return False

    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        adj =[[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[0]].append(prerequisite[1])
        
        ans =[]
        for query in queries:
            start , target = query[0],query[1]
            visited = [False]*numCourses
            ans.append(self.bfs(start,target,adj,visited))
        return ans 

#Method 2 : Using All pair shortest path (Floyd warshall Algorithm )

class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :r type: List[bool]
        """
        INT_MAX = float('inf')
        #Adj matrix would be of size V * V 
        adj = [[INT_MAX] * numCourses for _ in range(numCourses)]
        for i in range(numCourses):
            adj[i][i]=0 #No self loop 
        
        #Those have a connection make it 1 
        for edge in prerequisites:
            adj[edge[0]][edge[1]] =1 

        #Floyd warshall algorithm 
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if adj[i][k]==INT_MAX or adj[k][j]==INT_MAX:
                        continue
                    elif adj[i][k]+adj[k][j]<adj[i][j]:
                        adj[i][j]=adj[i][k]+adj[k][j]
        
        ans = []
        for query in queries :
            ans.append(adj[query[0]][query[1]]<INT_MAX)

        return ans

