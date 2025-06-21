#Question : Find the City With the Smallest Number of Neighbors at a Threshold Distance
#Link to the question:  https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        dist =[[float('inf')]*n for _ in range(n)]
        for i in range(n):
            dist[i][i]=0
        for edge in edges:
            u,v,w = edge[0],edge[1],edge[2]
            dist[u][v]=w
            dist[v][u]=w
        #Floyd warshall algorithmm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k]==float('inf') or dist[k][j]==float('inf'):
                        continue
                    dist[i][j]= min(dist[i][k]+dist[k][j],dist[i][j])
        
        cityCnt = n #Denotes the minimum no of city within threshold
        cityNum =-1
        for city in range(n):
            cnt =0
            for adjCity in range(n):
                if dist[city][adjCity]<=distanceThreshold:
                    cnt+=1
            if cnt<=cityCnt:
                cityCnt = cnt
                cityNum = city
        return cityNum