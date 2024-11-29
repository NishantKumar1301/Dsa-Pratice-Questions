#Question : Dijkstra Algorithm
#Link to the question: https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implementing-dijkstra-set-1-adjacency-matrix

from typing import List,Tuple
import heapq
class Solution:
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        #Step 1 : Calculate the number of vertices
        v = len(adj)
        
        #Step2 : Take the distance vector and initialize for all node as infinity except the souce node
        
        dist = [float("inf")]*v 
        
        dist[src]=0
        
        #Step3: Create a priority queue in the form of (distance,node) => Initialised with (distance=0,node = source)
        
        pq = [(0,src)] #(distance,vertex)
        
        # Dijkstra's algorithm:
        
        while pq:
            curr_dist , curr_node = heapq.heappop(pq)
            #If the current distance is greater than the previous distance then no need to update
            if curr_dist> dist[curr_node]:
                continue 
                
            #Check for all the adjacent node in its adjacency list
            for adj_node, weight in adj[curr_node]:
                # If a shorter path to adj_node is found, update the distance
                if weight + curr_dist < dist[adj_node]:
                    dist[adj_node]=curr_dist+weight
                    heapq.heappush(pq,(dist[adj_node],adj_node))
        
        return dist
                
        
        
        
        
