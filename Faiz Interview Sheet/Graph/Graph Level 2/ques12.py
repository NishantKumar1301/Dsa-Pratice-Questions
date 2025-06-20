#Question : Second Minimum Time to Reach Destination
#Link to the question: https://leetcode.com/problems/second-minimum-time-to-reach-destination/

from heapq import heappush, heappop
class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        adj =[[] for _ in range(n+1)]
        for edge in edges:
            u,v= edge[0],edge[1]
            adj[u].append(v)
            adj[v].append(u)
        dist1 = [float('inf')]*(n+1) #It stores the shortest distance from source to destination
        dist2 = [float('inf')]*(n+1) # It stores the second shortest distance from source to destination
        dist1[0]=0
        pq =[(0,1)]#time,node , here source node is 1
        while pq:
            timePassed, node = heappop(pq)
            if node==n and dist2[n]!=float('inf'):
                return dist2[n]
            div = timePassed//change
            #If div == odd then it is red signal and we have to wait till it becomes green
            if div%2==1:
                timePassed =(div+1)*change
            for ngbr in adj[node]:
                newTime = timePassed+ time
                #Case1 : the neighbour node is visited at the first time
                if newTime<dist1[ngbr]:
                    dist2[ngbr]=dist1[ngbr]
                    dist1[ngbr]=newTime
                    heappush(pq,(newTime,ngbr))
                #Case 2: the neigghbour node is visited at the second time ,
                #Update the dist2 if newTime's range is in between dist1[node],  dist2[node]
                elif dist1[ngbr]<newTime<dist2[ngbr]:
                    dist2[ngbr]=newTime
                    heappush(pq,(newTime,ngbr))
        return -1
            

