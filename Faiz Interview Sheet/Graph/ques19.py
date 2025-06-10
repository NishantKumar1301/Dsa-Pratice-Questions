#Question : All Ancestors of a Node in a Directed Acyclic Graph
#Link to the question: https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
from collections import deque
class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = deque()
        adj = [[] for _ in range(n)]
        indegree =[0]*n
        ans = [[] for _ in range(n)]
        #Creation OF Adjacency List
        for edge in edges:
            u,v = edge[0],edge[1]
            adj[u].append(v)
            indegree[v]+=1
        
        #Get The nodes in the topological order
        topoSort = []
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            topoSort.append(curr)
            for node in adj[curr]:
                indegree[node]-=1
                if indegree[node]==0:
                    queue.append(node)

        #Track ancestor of all nodes in topoOrder

        ancestor = [set() for _ in range(n)]
        #For each node of topoOrder put that node in its child node or adj[node]
        for parent in topoSort:
            for child in adj[parent]:
            #If the current node have parents too then in ancestor update its parent value(ancestors[parent])
                ancestor[child].add(parent)#Add is used bcoz it is set
                ancestor[child].update(ancestor[parent])#Update is used as for a set ancestor[parent ] will gives a list and add only inserts only one element in the set
            
        
        #Convert the sets to sorted list
        for i in range(n):
            ans[i]= sorted(ancestor[i])

        return ans