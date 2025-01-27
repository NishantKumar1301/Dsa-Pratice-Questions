#Question : Maximum Employees to Be Invited to a Meeting
#Link to the question: https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/description/

from collections import deque
class Solution(object):
    def bfs(self,start,adj,visited):
        queue = deque([(start,0)]) #(node,path_length)
        maxDistance = 0
        while queue:
            currNode , dist = queue.popleft()
            for neighbor in adj[currNode]:
                if not visited[neighbor]:
                    visited[neighbor]=True 
                    queue.append((neighbor,dist+1))
                    maxDistance = max(maxDistance,dist+1)
        return maxDistance

    def maximumInvitations(self, favorite):
        n = len(favorite)
        adj = [[] for _ in range(n)]
        for u in range(n):
            v= favorite[u]
            adj[v].append(u)
        longestCycle = happyCouple =0
        visited = [False]*n 
        for i in range(n):
            if not visited[i]:
                currNode , currNodeCount,mp = i, 0,{}
                #Find the length of the cycle 
                while not visited[currNode]:
                    visited[currNode]=True 
                    mp[currNode]=currNodeCount
                    currNodeCount+=1
                    nextNode = favorite[currNode]
                    if nextNode in mp:
                        #Cycle have been detected
                        cycleLength = currNodeCount - mp[nextNode]
                        longestCycle = max(longestCycle,cycleLength)
                        if cycleLength ==2:
                            #Case of happy couple
                            visitedNode = [False]*n
                            visitedNode[currNode]=True
                            visitedNode[nextNode]=True 
                            happyCouple+=2+ self.bfs(currNode,adj,visitedNode)+self.bfs(nextNode,adj,visitedNode)
                        break 
                    currNode = nextNode 
        return max(happyCouple,longestCycle)
