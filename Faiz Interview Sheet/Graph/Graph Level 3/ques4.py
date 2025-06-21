#Question : Number of Possible Sets of Closing Branches
#Link to the question:  https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

class Solution(object):
    def numberOfSets(self, n, maxDistance, roads):
        """
        :type n: int
        :type maxDistance: int
        :type roads: List[List[int]]
        :rtype: int
        """
        ans =0
        #n=3 , 000,001,010,100,101,110,111 
        # 010 means we have taken {1} but not {2,0}
        # 110 means we have taken {2,1} but not {0}
        for set in range(2**n):
            dist = [[float('inf')]*n for _ in range(n)]
            for i in range(n):
                dist[i][i]=0
            
            #Update the Graph based on the selected nodes - present in set
            for road in roads:
                u,v,w = road[0],road[1],road[2]
                if ((set>>u)&1) and ((set>>v)&1):
                    dist[u][v]=min(dist[u][v],w)
                    dist[v][u]= min(dist[v][u],w)

            #Floyd warshal algorithm
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if dist[i][k]!=float('inf') and dist[k][j]!=float('inf'):
                            dist[i][j]= min(dist[i][j],dist[i][k]+dist[k][j])
            
            #Check if all shortest paths <= maxDistance
            flag = True
            for i in range(n):
                for j in range(n):
                    if ((set>>i)&1) and ((set>>j)&1):
                        if dist[i][j]>maxDistance:
                            flag = False
                            break
                        
            if flag:
                ans+=1
            
        return ans

