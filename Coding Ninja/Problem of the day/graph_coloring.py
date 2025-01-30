#Question : Possible Bipartition
#Link to the question: https://leetcode.com/problems/possible-bipartition/description/

from collections import deque
class Solution(object):
    def bfs(self,node,adj,color):
        queue = deque([node])
        color[node]=1
        while queue:
            curr = queue.popleft()
            for ngbr in adj[curr]:
                if color[curr]==color[ngbr]:
                    return False
                if color[ngbr]==-1: #Means the neigbhour node have not been colored yet
                    color[ngbr]=1-color[curr]
                    queue.append(ngbr)
        return True
    def possibleBipartition(self, n, dislikes):
        adj =[[] for _ in range(n+1)]
        color =[-1]*(n+1)
        for dislike in dislikes:
            u , v = dislike[0],dislike[1]
            adj[u].append(v)
            adj[v].append(u)
        for i in range(1,n+1):
            if color[i]==-1:
                if not self.bfs(i,adj,color):
                    return False
        return True
        

